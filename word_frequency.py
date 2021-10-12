import collections

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from nltk.stem import WordNetLemmatizer
import string

from nltk.sentiment import SentimentIntensityAnalyzer


# MostCommonWords() finds the most common words in a text file
# Read input file, note the encoding is specified here
# It may be different in your text file

class MostCommonWords(object):
    def __init__(self):
        self.file = ""
        self.a = self.file

    def enter_file(self, file):
        self.file = open(file, encoding='cp1252')
        self.a = self.file.read()

    def lemmatiztion(self):
        lemmatizer = WordNetLemmatizer()
        return [' '.join([lemmatizer.lemmatize(word) for word in review.split()]) for review in self.file]

    def stopwords(self):
        stopwords = set(line.strip() for line in open('stopwords.txt'))
        stopwords = stopwords.union(set(['--', '-']))

        # print(stopwords)
        # Instantiate a dictionary, and for every word in the file,
        # Add to the dictionary if it doesn't exist. If it does, increase the count.
        wordcount = {}
        # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
        sia = SentimentIntensityAnalyzer()
        for word in self.a.lower().split():
            word = word.replace("“", "")  # remove quatation marks from text
            word = word.replace("”", "")
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")

            # ignore empty words from text
            if not len(word) == 0:
                # ignore numeric values from text
                if not word.isnumeric():
                    if word not in stopwords:
                        # Get the polarity score of each word
                        score = sia.polarity_scores(word)
                        # if the file is positive , add only those words that have polarity scora > 0
                        if (self.file.name == "PositiveText.txt"):
                            if (score['compound'] > 0):
                                if word not in wordcount:
                                    wordcount[word] = 1
                                else:
                                    wordcount[word] += 1
                        # if the file is negative , add only those words that have polarity scora <  0
                        elif (self.file.name == "NegativeText.txt"):
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
        for word, count in word_counter.most_common(10):  # (n_print):
            score = sia.polarity_scores(word)
            print(word, ": ", count, ":", score['compound'])

        # Close the file
        self.file.close()

        # Create a data frame of the most common words
        # Draw a bar chart
        lst = word_counter.most_common(10)  # (n_print)
        df = pd.DataFrame(lst, columns=['Word', 'Count'])
        ax = df.plot.bar(x='Word', y='Count')
        ax.bar_label(ax.containers[0])
        plt.xticks(rotation=20, horizontalalignment="center")
        plt.show()

#
# oj = MostCommonWords()
# oj.enter_file('PositiveText.txt')
# print(oj.lemmatiztion())
# oj.stopwords()
