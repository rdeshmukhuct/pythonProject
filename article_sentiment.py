from newspaper import Article, ArticleException
from matplotlib import pyplot as plt
from GoogleNews import GoogleNews
from textblob import TextBlob
import multiprocessing
import numpy as np
import time
import article_analysis

# nltk.download('punkt')
oc = article_analysis.GUIFunctions()


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

    @classmethod
    def parse_articles(cls, articles):
        article = Article(articles, fetch_images=False)
        article.download()
        try:
            article.parse()
            article.nlp()
        except:
            pass
        return article

    def analyze_sentence(self, article):
        analysis = TextBlob(article.text)
        self.analysis_polarity.append(analysis.polarity)
        return analysis

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

    def show_pie(self):
        data = [len(self.positive_list), len(self.negative_list), len(self.neutral_list)]
        oc.pie_chart(data)

    def store_sentiment_data(self):
        data = [len(self.positive_list), len(self.negative_list), len(self.neutral_list)]
        with open('data.txt', 'w') as f:
            for item in data:
                f.write("%d\n" % item)


if __name__ == '__main__':
    print("# of processors", multiprocessing.cpu_count())
    obj = ArticleSentiment('08/01/2010', '08/16/2021')
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
            f.write("%s\n" % item)

    with open('PositiveText.txt', 'w') as p:
        for item in obj.positive_list:
            p.write("%s\n" % item)

    # with open('NeutralText.txt', 'w') as n:
    #     for item in obj.neutral_list:
    #         n.write("%s\n" % item)

    print(len(obj.neutral_list))
    obj.store_sentiment_data()
