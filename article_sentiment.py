import pandas as pd
from newspaper import Article, ArticleException
from matplotlib import pyplot as plt
from GoogleNews import GoogleNews
from textblob import TextBlob
import multiprocessing
import numpy as np
import time

import MySQLDB
import article_analysis
import datetime as dt
from tkinter import *
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
import string
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import threading
import datetime

from nltk.tokenize.treebank import TreebankWordDetokenizer

nltk.download('vader_lexicon')

# download the stopwords
from nltk.corpus import stopwords

nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import SQLiteDB

nltk.download('punkt')
oc = article_analysis.GUIFunctions()
#db = SQLiteDB.SQLDb()
db = MySQLDB.MYSQLDb()


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

        self.time_s = []

        self.positive_counter = 0
        self.negative_counter = 0
        self.neutral_counter = 0
        self.sum_total_polarity = 0

    # This can also be change later. article_analysis.py has the same function
    # Read the documentation in article_analysis.py for more information
    def search_article_timeframe(self):
        google_news = GoogleNews()
        google_news.set_lang('en')
        google_news.set_time_range(self.start_date, self.end_date)
        google_news.set_encode('utf-8')
        # google_news.get_news('UCTT ham-let ltd')
        # google_news.search('UCTT ham-let ltd')
        google_news.get_news('UCTT')
        google_news.search('UCTT')
        self.links = google_news.get_links()
        result = google_news.result()
        protocol = 'https://'  # appends the protocol if the url if the url is missing it.
        self.url = np.array([protocol + domain if protocol not in domain else domain for domain in self.links])
        db.insert_data_articles(result, self.url)
        # db.get_data()

    # SQL call here
    # parse_articles() takes one argument which is the text file from the list and returns the processed article
    # This is the most costly and time consuming function in the class, because of parse() and nlp() which
    # take the most amount of time to compute. time to compute is usually greater than 70 seconds
    @classmethod
    def parse_articles(cls, articles):
        article = Article(articles, fetch_images=False)
        article.download()
        try:
            article.parse()
            # text = TextBlob(article.text)
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
        for articles in loop:
            parsed_article = self.parse_articles(articles)

            analysis = self.analyze_sentence(parsed_article)  # returns the analyzed version of the article

            print("From Lex", analysis.polarity)
            self.time_s.append(analysis.polarity)

            self.thing.append(parsed_article)  # addition
            self.sum_total_polarity += analysis.polarity
            self.summary.append(parsed_article.summary)

            # For better sentimental analysis result, we will preprocess data,
            # and use SentimentIntensityAnalyzer from nltk
            # lower case, remove punctuations and stop words
            for sentence in analysis.sentences:
                analysis = str(sentence)
                # pre processing data nlp
                # lower case
                analysis = analysis.lower()

                try:
                    # remove punctuations
                    analysis = analysis.translate(str.maketrans('', '', string.punctuation))
                    analysis = str(analysis)

                    # tokenize the sentence
                    text_tokens = word_tokenize(analysis)

                    # remove those stop words from the list that might change the meaning of the sentence
                    # Example : John doesn't like to swim will not be converted to John like to swim
                    to_remove = ['no', 'not', 'don\'t', 'didn\'t', 'did\'t'
                        , 'hasn\'t', 'hadn\'t', 'hasn\'t', 'wasn\'t',
                                 'couldn\'t', 'haven\'t', 'doesn\'t',
                                 'won\'t', 'wouldn\'t', 'weren\'t']
                    stopwords = set(nltk.corpus.stopwords.words('english')).difference(to_remove)
                    # remove stop words from the text
                    tokens_without_sw = [word for word in text_tokens if not word in stopwords]
                    # detokenize conver the tokenize version of text into normal sentence without stopwords
                    text = TreebankWordDetokenizer().detokenize(tokens_without_sw)

                    # get the sentimental score
                    sia = SentimentIntensityAnalyzer()
                    score = sia.polarity_scores(text)

                    # positive
                    if score['compound'] > 0:
                        self.positive_counter += 1
                        self.positive_list.append(text)
                    # negative
                    elif score['compound'] < 0:
                        self.negative_counter += 1
                        self.negative_list.append(text)
                    # neutral
                    else:
                        self.neutral_counter += 1
                        self.neutral_list.append(text)
                except Exception as e:
                    print(e)

    # show_stats(): takes zero arguments
    # This function displays information about the scraped articles after they have been parsed and passed through the
    # natural language processor
    # Shows the number of positive/negative/neutral sentiment sentences in each article,
    # Mean score of all the articles, and sum total
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

    def time_series(self):

        time = [i for i in range(0, len(self.time_s))]

        #data = pd.DataReader(None, None, self.start_date, self.end_date)
        #data['Date'] = data['Date'].map(mdates.date2num)
        #data = [datetime.datetime(2021,i, 1, 0) for i in range(50)]

        df_time_series = pd.DataFrame({'Article': time, 'Sentiment': self.time_s})
        df_time_series.plot('Article', 'Sentiment')

    # This function can be removed because article_analysis.py has a pie chart function that does the same thing.
    def show_pie(self):
        data = [len(self.positive_list), len(self.negative_list), len(self.neutral_list)]
        oc.pie_chart(data)

    # store_sentiment_data() saves then length of each sentiment to a text file so GUI.py can use it for UX
    def store_sentiment_data(self):
        data = [len(self.positive_list), len(self.negative_list), len(self.neutral_list)]

        # sqlite ???? insert_occurances ???
        with open('TextFiles/data.txt', 'w') as f:
            for item in data:
                f.write("%d\n" % item)


# if trying to run this with multiprocessing you must use the following command for it to run
# if __name__ == '__main__':

# added the feature where instead of hardcoded the dates the user can select the dates and
# the articles will be scraped based on that dates
if __name__ == '__main__':
    def call():
        from_date = cal_from.get_date()
        to_date = cal_to.get_date()
        print("# of processors", multiprocessing.cpu_count())
        obj = ArticleSentiment(from_date, to_date)
        obj.search_article_timeframe()
        begin = time.time()

        # Get the total number of articles and divide by number of threads
        length = (len(obj.url)) / 8
        length = int(length)

        tlist1 = list()
        tlist2 = list()
        tlist3 = list()
        tlist4 = list()
        tlist5 = list()
        tlist6 = list()
        tlist7 = list()
        tlist8 = list()

        # Store all the urls in different list so that later can be passed to different threads
        count = 0
        for url in obj.url:
            if count == length:
                break
            else:
                tlist1.append(obj.url[count])
                tlist2.append(obj.url[count + length])
                tlist3.append(obj.url[count + (2 * length)])
                tlist4.append(obj.url[count + (3 * length)])
                tlist5.append(obj.url[count + (4 * length)])
                tlist6.append(obj.url[count + (5 * length)])
                tlist7.append(obj.url[count + (6 * length)])
                tlist8.append(obj.url[count + (7 * length)])
                count += 1

        # Creatin multiple threads and passing in different urls
        t1 = threading.Thread(target=obj.lexical_article_analyze, args=(tlist1,))
        t2 = threading.Thread(target=obj.lexical_article_analyze, args=(tlist2,))
        t3 = threading.Thread(target=obj.lexical_article_analyze, args=(tlist3,))
        t4 = threading.Thread(target=obj.lexical_article_analyze, args=(tlist4,))
        t5 = threading.Thread(target=obj.lexical_article_analyze, args=(tlist5,))
        t6 = threading.Thread(target=obj.lexical_article_analyze, args=(tlist6,))
        t7 = threading.Thread(target=obj.lexical_article_analyze, args=(tlist7,))
        t8 = threading.Thread(target=obj.lexical_article_analyze, args=(tlist8,))

        # Start all threads
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()

        # Wait for all threads to finish
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()

        end = time.time()

        obj.time_series()
        obj.show_stats()
        obj.show_pie()

        print("Total Runtime of the Program is: {:.2f} seconds".format(end - begin))

        # here we can call the sqlite method to update the positive, negative and neutral tables.
        #  sqlite ???? insert data(obj.positive_list)

        db.insert_data_neutral(obj.neutral_list)
        db.insert_data_negative(obj.negative_list)
        db.insert_data_positive(obj.positive_list)
        db.close()

        obj.store_sentiment_data()


    # Instead of hardcoding the dates we will provide the option to the user
    # to select dates and the articles will be scraped based on
    # these dates.
    root = Tk()
    root.title("Reviews")
    label_from = Label(root, text='From:', font='Roboto')
    label_from.pack()
    cal_from = DateEntry(root, width=50, year=2020, month=1, day=1)
    cal_from.pack(padx=10, pady=10)

    label_to = Label(root, text="To:", font='Roboto')
    label_to.pack()
    cal_to = DateEntry(root, width=50)
    cal_to.pack(padx=10, pady=10)

    btn_call = Button(root, text="Submit", font='Roboto', command=call)
    btn_call.pack()
    root.mainloop()
