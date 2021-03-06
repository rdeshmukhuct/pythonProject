import collections
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from nltk.stem import WordNetLemmatizer
import string

from nltk.sentiment import SentimentIntensityAnalyzer

import MySQLDB

db = MySQLDB.MYSQLDb()



# MostCommonWords() finds the most common words in a text file
# Read input file, note the encoding is specified here
# It may be different in your text file

class MostCommonWords(object):
    def __init__(self):
        self.a = ""
    def lemmatiztion(self):
        lemmatizer = WordNetLemmatizer()
        return [' '.join([lemmatizer.lemmatize(word) for word in review.split()]) for review in self.file]

    def stopwords(self, emotion):
        stopwords = set(line.strip() for line in open('TextFiles/stopwords.txt'))
        stopwords = stopwords.union(set(['--', '-']))

        # print(stopwords)
        # Instantiate a dictionary, and for every word in the file,
        # Add to the dictionary if it doesn't exist. If it does, increase the count.
        wordcount = {}
        if emotion == "pos":
            rows = db.getPositiveTexts()
            listTexts = list()
            for row in rows:
                listTexts.append(row[0])

            # print(listTexts)
            self.a = ""
            self.a = '.'.join(listTexts)
        elif emotion == "neg":
            rows = db.getNegativeTexts()
            listTexts = list()
            for row in rows:
                listTexts.append(row[0])

            # print(listTexts)
            self.a = ""
            self.a = '.'.join(listTexts)
        elif emotion == "neutr":
            rows = db.getNeutralTexts()
            listTexts = list()
            for row in rows:
                listTexts.append(row[0])

            # print(listTexts)
            self.a = ""
            self.a = '.'.join(listTexts)






        # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
        sia = SentimentIntensityAnalyzer()
        for word in self.a.lower().split():
            word = word.replace("???", "")  # remove quatation marks from text
            word = word.replace("???", "")
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("???????", "")
            word = word.replace("???????", "")
            word = word.replace("*", "")

            # ignore empty words from text
            if not len(word) == 0:
                # ignore numeric values from text
                if not word.isnumeric():
                    if word not in stopwords:
                        # Get the polarity score of each word
                        score = sia.polarity_scores(word)
                        # if the file is positive , add only those words that have polarity scora > 0
                        if emotion == "pos":
                            if (score['compound'] > 0):
                                if word not in wordcount:
                                    wordcount[word] = 1
                                else:
                                    wordcount[word] += 1
                        # if the file is negative , add only those words that have polarity scora <  0
                        elif emotion == "neg":
                            if (score['compound'] < 0):
                                if word not in wordcount:
                                    wordcount[word] = 1
                                else:
                                    wordcount[word] += 1
                        # if the file is neutral , add only those words that have polarity scora =  0
                        else:
                            if word not in wordcount:
                                wordcount[word] = 1
                            else:
                                wordcount[word] += 1

        # Print most common word
        # n_print = int(input("How many most common words to print: "))
        # print("\nOK. The {} most common words are as follows\n".format(n_print))
        word_counter = collections.Counter(wordcount)
        word_list = []
        words = []
        for word, count in word_counter.most_common(10):  # (n_print):
            score = sia.polarity_scores(word)
            print(word, ": ", count, ":", score['compound'])
            word_list.append(count)
            words.append(word)

        for w in word_list:
            print(w)
        X = words
        data = word_list

        X_axis = np.arange(len(X))

        plt.bar(X_axis - 0.2, data, 0.4, label='Words')

        plt.xticks(X_axis, X, rotation=45)

        plt.legend()
        plt.show()

#
# oj = MostCommonWords()
# oj.enter_file('PositiveText.txt')
# print(oj.lemmatiztion())
# oj.stopwords()