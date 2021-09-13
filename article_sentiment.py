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
import matplotlib.dates as mdates
import pandas_datareader as web
from mplfinance.original_flavor import candlestick_ochl

# nltk.download('punkt')
oc = article_analysis.GUIFunctions()


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
        google_news.get_news('UCTT ham-let ltd')
        google_news.search('UCTT ham-let ltd')
        self.links = google_news.get_links()
        protocol = 'https://'  # appends the protocol if the url if the url is missing it.
        self.url = np.array([protocol + domain if protocol not in domain else domain for domain in self.links])

    # parse_articles() takes one argument which is the text file from the list and returns the processed article
    # This is the most costly and time consuming function in the class, because of parse() and nlp() which
    # take the most amount of time to compute. time to compute is usually greater than 70 seconds
    @classmethod
    def parse_articles(cls, articles):
        article = Article(articles, fetch_images=False)
        article.download()
        try:
            article.parse()
            text = TextBlob(article.text)
            # added this just to get the entire text from all the articles that  we have scraped
            with open('EntireText.txt', 'a') as e:
                try:
                    e.write("%s\n" % text)
                except:
                    pass

            article.nlp()
            # added this to get the summary of all the articles
            with open('SummaryText.txt', 'a') as s:
                try:
                    s.write("%s\n" % text)
                except:
                    pass
        except:
            pass
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
    def lexical_article_analyze(self, loop):
        for articles in loop:
            parsed_article = self.parse_articles(articles)

            analysis = self.analyze_sentence(parsed_article)  # returns the analyzed version of the article
            self.thing.append(parsed_article)  # addition
            self.sum_total_polarity += analysis.polarity
            self.summary.append(parsed_article.summary)

            for sentence in analysis.sentences:
                if sentence.polarity > 0:
                    self.positive_counter += 1
                    self.positive_list.append(sentence)
                elif sentence.polarity < 0:
                    self.negative_counter += 1
                    self.negative_list.append(sentence)
                else:
                    self.neutral_counter += 1
                    self.neutral_list.append(sentence)

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

    # This function can be removed because article_analysis.py has a pie chart function that does the same thing.
    def show_pie(self):
        data = [len(self.positive_list), len(self.negative_list), len(self.neutral_list)]
        oc.pie_chart(data)

    # store_sentiment_data() saves then length of each sentiment to a text file so GUI.py can use it for UX
    def store_sentiment_data(self):
        data = [len(self.positive_list), len(self.negative_list), len(self.neutral_list)]
        with open('data.txt', 'w') as f:
            for item in data:
                f.write("%d\n" % item)


# if trying to run this with multiprocessing you must use the following command for it to run
# if __name__ == '__main__':

# added the feature where instead of hardcoding the dates the user can select the dates and
# the articles will be scraped based on that dates
if __name__ == '__main__':
    def call ():
        from_date = cal_from.get_date()
        to_date = cal_to.get_date()
        print("# of processors", multiprocessing.cpu_count())
        obj = ArticleSentiment(from_date, to_date)
        obj.search_article_timeframe()

        begin = time.time()
        p1 = multiprocessing.Process(target=obj.lexical_article_analyze(obj.url))
        p1.start()
        p1.join()
    # obj.lexical_article_analyze(obj.url)

    # stats = DisplayStat()
        obj.show_stats()
        obj.show_pie()

        end = time.time()
        print("Total Runtime of the Program is: {:.2f} seconds".format(end - begin))

        with open('NegativeText.txt', 'w') as f:
            for item in obj.negative_list:
                try:
                    f.write("%s\n" % item)
                except:
                     pass

        with open('PositiveText.txt', 'w') as p:
            for item in obj.positive_list:
                try:
                    p.write("%s\n" % item)
                except:
                     pass

        with open('NeutralText.txt', 'w') as n:
            for item in obj.neutral_list:
                try:
                    n.write("%s\n" % item)
                except:
                    pass

        print(len(obj.neutral_list))
        obj.store_sentiment_data()
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
