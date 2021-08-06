import statistics
from matplotlib import pyplot as plt
import numpy as np
from textblob import TextBlob
import nltk
from newspaper import Article, ArticleException
from GoogleNews import GoogleNews
import multiprocessing
import numpy as np
import time


# This is the main source code.
# nltk.download('punkt')


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

        self.google_bucket = []
        self.yahoo_bucket = []
        self.bucket_1 = []
        self.bucket_2 = []

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
        # self.yahoo_bucket = [domain_yahoo for domain_yahoo in self.url if 'yahoo' in domain_yahoo]
        # self.google_bucket = [domain_google for domain_google in self.url if 'google' in domain_google]
        # quarter = len(self.url) // 4
        #
        # s1 = self.url[0:quarter]
        # s2 = self.url[quarter:quarter * 2]
        # s3 = self.url[(quarter * 2): quarter * 3]
        # s4 = self.url[(quarter * 3): -1]
        #
        # self.yahoo_bucket = s1
        # self.google_bucket = s2
        # self.bucket_1 = s3
        # self.bucket_2 = s4

    def analyze_sentence(self, article):
        analysis_polarity_append = self.analysis_polarity.append  # optimization
        analysis = TextBlob(article.text)
        analysis_polarity_append(analysis.polarity)
        return analysis

    def lexical_article_analyze(self):

        pos_append = self.positive_list.append  # optimization
        neg_append = self.negative_list.append  # optimization
        neu_append = self.neutral_list.append  # optimization
        summary_append = self.summary.append  # optimization

        for articles in self.url:
            parsed_article = parse_articles(articles)  # This will return a version of the article that is pre-processed

            analysis = self.analyze_sentence(parsed_article)  # returns the analyzed version of the article
            self.sum_total_polarity += analysis.polarity
            summary_append(parsed_article.summary)

            analysis_sentences = analysis.sentences  # optimization

            for sentence in analysis_sentences:
                if sentence.polarity > self.NEUTRAL_VALUE:
                    self.positive_counter += 1
                    pos_append(sentence)
                elif sentence.polarity < self.NEUTRAL_VALUE:
                    self.negative_counter += 1
                    neg_append(sentence)
                else:
                    self.neutral_counter += 1
                    neu_append(sentence)

    def show_stats(self):
        print("Date Range from {} to {}".format(self.start_date, self.end_date))
        print("TotalNumber of Articles Used: {}".format(len(self.url)))
        # print("Number of Articles Used: {}".format(len(self.yahoo_bucket + self.google_bucket + self.bucket_1 +
        # self.bucket_2)))
        total_review_sentences = (self.positive_counter + self.negative_counter + self.neutral_counter)
        print("Total Reviewed Sentences: {}".format(total_review_sentences))
        print("Positive Sentences: {}".format(self.positive_counter))
        print("Negative Sentences: {}".format(self.negative_counter))
        print("Neutral Sentences: {}".format(self.neutral_counter))
        print("Sum Total Article Review: {:.2f}".format(self.sum_total_polarity))
        print("Average Score Review: {:.3}".format(self.sum_total_polarity / len(self.links)))

    #   print("Standard Deviation Between Article: {:.3f}".format(statistics.stdev(self.analysis_polarity)))
    #   print("Variance Between Article: {:.3f}".format(
    #   statistics.variance(self.analysis_polarity, statistics.mean(self.analysis_polarity))))

    def show_histogram(self):
        a = np.array(self.analysis_polarity)
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.hist(a, bins='auto')
        plt.title("Individual Article Sentiment")
        plt.close('all')


if __name__ == '__main__':
    begin1 = time.time()

    obj = ArticleSentiment('01/01/2021', '01/13/2021')
    obj.search_article_timeframe()

    end1 = time.time()
    ############################################################

    begin = time.time()
    # p1 = multiprocessing.Process(target=obj.lexical_article_analyze(obj.yahoo_bucket))
    # p2 = multiprocessing.Process(target=obj.lexical_article_analyze(obj.google_bucket))
    # p3 = multiprocessing.Process(target=obj.lexical_article_analyze(obj.bucket_1))
    # p4 = multiprocessing.Process(target=obj.lexical_article_analyze(obj.bucket_2))
    #
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    #
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    obj.lexical_article_analyze()

    obj.show_stats()
    # obj.show_histogram()
    print("Computed")

    # time.sleep(1)
    end = time.time()
    print("Total Runtime of the Program is: {:.2f} seconds".format(end - begin))
    print("Total Runtime of the Program is: {:.2f} seconds".format(end1 - begin1))
    print("1", len(obj.yahoo_bucket))
    print("2", len(obj.google_bucket))
    print("3", len(obj.bucket_1))
    print("4", len(obj.bucket_2))
