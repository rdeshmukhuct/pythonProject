from collections import Counter
import statistics

import newspaper
from matplotlib import pyplot as plt
import numpy as np
from textblob import TextBlob
import nltk
from newspaper import Article, ArticleException
from GoogleNews import GoogleNews
import csv
import multiprocessing

nltk.download('punkt')

google_news = GoogleNews()


def alpha_save_text(p_article):
    file1 = open("files/NewFile.txt", "a")
    file1.writelines(p_article)


class ArticleAnalysis:

    def __init__(self):
        self.NEUTRAL_VALUE = 0  # Constant Value to be used in conditional statements

        self.positive_list = []  # this list holds the polarity of a article/blog. Any positive sentence is placed
        # into p:= positive
        self.negative_list = []  # neg := negative, saves any negative sentence
        self.neutral_list = []  # n := neutral, sentences
        self.analysis_polarity = []  # saves the numerical value of the article polarity.
        self.summary = []

        self.positive_counter = 0
        self.negative_counter = 0
        self.neutral_counter = 0
        self.sum_total_polarity = 0

        self.cnn_paper = newspaper.build('http://cnn.com')

    def analyze_s(self, article):
        analysis = TextBlob(article.text)
        alpha_save_text(analysis)
        self.analysis_polarity.append(analysis.polarity)
        return analysis

    def parse_a(self, articles):
        article = Article(articles.decode())
        article.download()
        article.parse().decode()
        article.nlp()
        return article

    def lexical_article_a(self):
        for articles in self.cnn_paper.articles:
            parsed_article = self.parse_a(articles)
            # This will return a version of the article that is
            # pre-processed

            analysis = self.analyze_s(parsed_article)  # returns the analyzed version of the article
            self.sum_total_polarity += analysis.polarity  #
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

    def show_s(self):
       # print("Number of Articles Used: {}".format(len(self.url)))
        total_review_sentences = (self.positive_counter + self.negative_counter + self.neutral_counter)
        print("Total Reviewed Sentences: {}".format(total_review_sentences))
        print("Positive Sentences: {}".format(self.positive_counter))
        print("Negative Sentences: {}".format(self.negative_counter))
        print("Neutral Sentences: {}".format(self.neutral_counter))
        print("Sum Total Article Review: {:.2f}".format(self.sum_total_polarity))
        # print("Average Score Review: {:.3}".format(self.sum_total_polarity / len(self.url)))
        # print("Standard Deviation Between Article: {:.3f}".format(statistics.stdev(self.analysis_polarity)))
        # print("Variance Between Article: {:.3f}".format(statistics.variance(self.analysis_polarity, statistics.mean(self.analysis_polarity))))




# pd = ArticleSentiment()
# split_it = pd.negative_counter.split()
# Counter = Counter(split_it)
# most_occur = Counter.most_common(4)
# print(most_occur)

ob = ArticleAnalysis()
ob.lexical_article_a()
ob.show_s()
# alpha_save_text()


