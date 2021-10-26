from newspaper import Article, ArticleException
from matplotlib import pyplot as plt
from GoogleNews import GoogleNews
from textblob import TextBlob
import multiprocessing
import numpy as np
import time
import article_analysis
import datetime as dt
from tkinter import *
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
import string
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import threading

from nltk.tokenize.treebank import TreebankWordDetokenizer

# nltk.download('vader_lexicon')

# download the stopwords
# from nltk.corpus import stopwords
# nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import SQLiteDBModified
import MySQLDatabaseModified
db = MySQLDatabaseModified.MySQLDbModified()

#db = SQLiteDBModified.SQLDbModified()



# ReadMe -> This class analyzes the polarity and sentiment of each article scarped form the internet
# the ranking system is on a scale from [-1, 1] with 0 in between.
# When the value is Zero the article sentiment is Neutral
# if the value is within the range of (0, 1] then sentiment is positive and the closer the value is to 1 the stronger
# if the value is withing the range of [-1, 0) then sentiment is negative and the closer to -1 the more negative it is.

class ArticleSentiment:

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

        self.positive_list = []  # this list holds the polarity of a article
        self.negative_list = []  # neg := negative, saves any negative sentence
        self.neutral_list = []  # n := neutral, sentences
        self.analysis_polarity = []  # saves the numerical value of the article polarity.
        self.summary = []
        self.links = []
        self.url = np.array([])
        self.thing = []
        self.result = []

        self.positive_counter = 0
        self.negative_counter = 0
        self.neutral_counter = 0
        self.sum_total_polarity = 0

        # Create all the tables required

        self.list_of_months = ["january_sentiments", "february_sentiments", "march_sentiments", "april_sentiments",
                               "may_sentiments", "june_sentiments", "july_sentiments", "august_sentiments",
                               "september_sentiments", "october_sentiments"]
        self.list_of_months_description = ["january_description", "february_description", "march_description", "april_description",
                               "may_description", "june_description", "july_description", "august_description",
                               "september_description", "october_description"]
        # Create all the month tables
        for month in self.list_of_months:
            db.create_month_sentiments(month)
        for month in self.list_of_months_description:
            db.create_month_description(month)

    # This can also be change later. article_analysis.py has the same function
    # Read the documentation in article_analysis.py for more information
    def search_article_timeframe(self):
        google_news = GoogleNews()
        google_news.set_lang('en')
        google_news.set_time_range('09/01/2021', '09/30/2021')
        google_news.set_encode('utf-8')

        # google_news.get_news('UCTT')      # Cannot use this for time range
        google_news.search('UCTT')
        self.links = google_news.get_links()
        self.result = google_news.result(sort=True)
        protocol = 'https://'  # appends the protocol if the url if the url is missing it.
        # self.url = np.array([protocol + domain if protocol not in domain else domain for domain in self.links])
        print("End of search")

        for result in self.result:
            print(result['title'])

        # SQL call here
        # parse_articles() takes one argument which is the text file from the list and returns the processed article
        # This is the most costly and time consuming function in the class, because of parse() and nlp() which
        # take the most amount of time to compute. time to compute is usually greater than 70

    def set_month(self):

        start_month = '09/01/2021'
        end_month = '09/30/2021'
        month_value = start_month.split('/')
        value = int(month_value[0])

        return self.list_of_months[value-1]

    def set_month_description(self):

        start_month = '09/01/2021'
        end_month = '09/30/2021'
        month_value = start_month.split('/')
        value = int(month_value[0])

        return self.list_of_months_description[value - 1]



    @classmethod
    def parse_articles(cls, articles):
        article = Article(articles, fetch_images=False)
        article.download()
        try:
            article.parse()
            text = TextBlob(article.text)
            article.nlp()
        except Exception as e:
            print(e)
        return article

    # analyze_sentence(): takes one argument index from list and returns the analysis in the index
    # this function is called by lexical_article_analyze()
    def analyze_sentence(self, article):
        analysis = TextBlob(article.text)
        self.analysis_polarity.append(analysis.polarity)
        return analysis

    # lexical_article_analyze(): takes one argument in the form of a list, and returns nothing.
    # This function calls upon two other functions within article_sentiment.py
    # It calls ArticleSentiment.parsed_articles() and then ArticleSentiment.analyze_sentence()
    # The main purpose of this function is to parse and analyze the scraped articles form the internet
    # Once the articles ae parsed its then append into its sentiment list in the second for loop.
    # loop here contains the links to all the articles
    def lexical_article_analyze(self, loop):
        #counter = 0
        for articles in loop:
            print("The current article link is : ", articles['link'])
            # values to be inserted to our table
            link_param = str(articles['link'])
            title_param = str(articles['title'])
            date_param = str(articles['datetime'])

            parsed_article = self.parse_articles(articles['link'])


            analysis = self.analyze_sentence(parsed_article)  # returns the analyzed version of the article
            text = analysis.split()

            # Just checking of the artilce that we are getting from the internet
            # is about UCTT by checking if the UCTT/Ultra/Ham -Let word appears more than 4 time
            checkString = 'UCTT'
            checkString1 = 'Ultra'
            checkString2 = 'Ham - Let'
            count1 = text.count(checkString)
            count2 = text.count(checkString1)
            count3 = text.count(checkString2)
            total_count = count3 + count2 + count1
            # if the word UCTT or Ham - Let or Ultra Clean Holdings appear more
            # than 3 times then only we go ahead and insert into our table.
            if total_count > 3 or total_count == 3:
                self.thing.append(parsed_article)  # addition
                article_polarity = 0
                article_polarity = analysis.polarity  # get the polarity score of the article
                self.sum_total_polarity += analysis.polarity
                self.summary.append(parsed_article.summary)

                #  Reset the list
                self.positive_list = list()
                self.negative_list = list()
                positive_sentences = 0
                negative_sentences = 0

                for sentence in analysis.sentences:
                    analysis = str(sentence)

                    try:
                        # get the sentimental score
                        score = TextBlob(analysis).sentiment.polarity

                        if (score > 0):
                            positive_sentences += 1
                            self.positive_counter += 1
                            self.positive_list.append(analysis)
                            self.positive_list.append(("\n"))
                        if (score < 0):
                            negative_sentences += 1
                            self.negative_counter += 1
                            self.negative_list.append(analysis)
                            self.negative_list.append("\n")

                    except Exception as e:
                        print(e)
                # Insert into database
                if (positive_sentences > 0 or negative_sentences > 0):
                    pos = ''.join(self.positive_list)
                    neg = ''.join(self.negative_list)

                    # for i in self.list_of_months:
                    # month = self.list_of_months[counter]
                    print(self.set_month())
                    print(self.set_month_description())
                    print("Here")
                    print(title_param, date_param, link_param, positive_sentences, negative_sentences, article_polarity)
                    db.insert_month_description(self.set_month_description(), title_param, date_param, link_param,
                                                positive_sentences, negative_sentences,
                                                article_polarity)
                    # db.insert_month_description(self.set_month_description(), title_param, date_param, link_param, positive_sentences,negative_sentences,article_polarity)
                    db.insert_month_sentiments(self.set_month(), title_param, date_param, pos, neg)
                    # print(month)
                    # counter += 1




    # show_stats(): takes zero arguments This function displays information about the scraped articles after they
    # have been parsed and passed through the natural language processor Shows the number of
    # positive/negative/neutral sentiment sentences in each article, Mean score of all the articles, and sum total
    def show_stats(self):
        total_review_sentences = (self.positive_counter + self.negative_counter + self.neutral_counter)
        print("Date Range from {} to {}".format(self.start_date, self.end_date))
        print("TotalNumber of Articles Used: {}".format(len(self.url)))
        print("Total Reviewed Sentences: {}".format(total_review_sentences))
        print("Positive Sentences: {}".format(self.positive_counter))
        print("Negative Sentences: {}".format(self.negative_counter))
        print("Neutral Sentences: {}".format(self.neutral_counter))
        print("Sum Total Article Review: {:.2f}".format(self.sum_total_polarity))
        print("Average Score Review: {:.3}".format(self.sum_total_polarity / len(self.links)))

    # show_histogram(): takes zero arguments and returns nothing
    # shows a histogram of article polarity
    def show_histogram(self):
        a = np.array(self.analysis_polarity)
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.hist(a, bins='auto')
        plt.title("Individual Article Sentiment")
        plt.show()

    # This function can be removed because article_analysis.py has a pie chart function that does the same thing.
    def show_pie(self):
        data = [len(self.positive_list), len(self.negative_list), len(self.neutral_list)]
        # oc.pie_chart(data)

    # store_sentiment_data() saves then length of each sentiment to a text file so GUI.py can use it for UX
    def store_sentiment_data(self):
        data = [len(self.positive_list), len(self.negative_list), len(self.neutral_list)]

        # sqlite ???? insert_occurances ???
        with open('TextFiles/data.txt', 'w') as f:
            for item in data:
                f.write("%d\n" % item)

    # if trying to run this with multiprocessing you must use the following command for it to run
    # if __name__ == '__main__':


if __name__ == '__main__':
    obj = ArticleSentiment('09/01/2021', '09/30/2021')
    obj.search_article_timeframe()
    obj.lexical_article_analyze(obj.result)