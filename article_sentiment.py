import concurrent.futures
import multiprocessing
from matplotlib import pyplot as plt
from textblob import TextBlob
from newspaper import Article, ArticleException
from GoogleNews import GoogleNews
import numpy as np
from operator import methodcaller
import statistics
import time
import nltk


# This is the main source code.
nltk.download('punkt')


def beta_save_text(p_article):
    file1 = open("NewFile.txt", "a")
    file1.writelines(p_article)


def parse_articles(articles):
    article = Article(articles)
    article.download()
    try:
        article.parse()
        article.nlp()
    except:
        pass
    return article


class ArticleSentiment:

    def __init__(self, start_date, end_date):
        self.NEUTRAL_VALUE = 0  # Constant Value to be used in conditional statements
        self.start_date = start_date
        self.end_date = end_date

        self.positive_list = []  # this list holds the polarity of a article
        self.negative_list = []  # neg := negative, saves any negative sentence
        self.neutral_list = []  # n := neutral, sentences
        self.analysis_polarity = []  # saves the numerical value of the article polarity.
        self.summary = []
        self.links = []

        self.url = np.array([])
        self.google_bucket = np.array([])
        self.yahoo_bucket = np.array([])

        self.positive_counter = 0
        self.negative_counter = 0
        self.neutral_counter = 0
        self.sum_total_polarity = 0

    def search_article_timeframe(self):
        google_news = GoogleNews()
        google_news.set_lang('en')
        google_news.set_time_range(self.start_date, self.end_date)
        google_news.set_encode('utf-8')
        google_news.get_news('UCTT')
        google_news.search('UCTT')
        self.links = google_news.get_links()
        protocol = 'https://'  # appends the protocol if the url if the url is missing it.
        self.url = np.array([protocol + domain if protocol not in domain else domain for domain in self.links])
        # self.yahoo_bucket = np.array([domain_yahoo for domain_yahoo in self.url if 'yahoo' in domain_yahoo])
        # self.google_bucket = np.array([domain_google for domain_google in self.url if 'google' in domain_google])

    def analyze_sentence(self, article):
        analysis = TextBlob(article.text)
        self.analysis_polarity.append(analysis.polarity)
        return analysis

    def lexical_article_analyze(self, loop):
        for articles in loop:
            parsed_article = parse_articles(articles)  # This will return a version of the article that is pre-processed

            analysis = self.analyze_sentence(parsed_article)  # returns the analyzed version of the article
            self.sum_total_polarity += analysis.polarity
            self.summary.append(parsed_article.summary)

            for sentence in analysis.sentences:
                if sentence.polarity > self.NEUTRAL_VALUE:
                    self.positive_counter += 1
                    self.positive_list.append(sentence)
                elif sentence.polarity < self.NEUTRAL_VALUE:
                    self.negative_counter += 1
                    self.negative_list.append(sentence)
                else:
                    self.neutral_counter += 1
                    self.neutral_list.append(sentence)

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

    def show_histogram(self):
        a = np.array(self.analysis_polarity)
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.hist(a, bins='auto')
        plt.title("Individual Article Sentiment")
        plt.show()


if __name__ == '__main__':
    print("#of processors", multiprocessing.cpu_count())
    obj = ArticleSentiment('08/11/2010', '08/11/2021')
    obj.search_article_timeframe()
    begin = time.time()

    p1 = multiprocessing.Process(target=obj.lexical_article_analyze(obj.url))
    # p2 = multiprocessing.Process(target=obj.lexical_article_analyze(obj.google_bucket))
    # p3 = multiprocessing.Process(target=obj.lexical_article_analyze(obj.bucket_1))
    # p4 = multiprocessing.Process(target=obj.lexical_article_analyze(obj.bucket_2))

    p1.start()
    # p2.start()
    # p3.start()
    # p4.start()

    p1.join()
    # p2.join()
    # p3.join()
    # p4.join()

    obj.show_stats()

    end = time.time()
    print("Total Runtime of the Program is: {:.2f} seconds".format(end - begin))
