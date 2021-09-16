import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer


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
        # Instantiate a dictionary, and for every word in the file,
        # Add to the dictionary if it doesn't exist. If it does, increase the count.
        wordcount = {}
        # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
        for word in self.a.lower().split():
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")
            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1

        # Print most common word
        # n_print = int(input("How many most common words to print: "))
        # print("\nOK. The {} most common words are as follows\n".format(n_print))
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(10):  # (n_print):
            print(word, ": ", count)

        # Close the file
        self.file.close()

        # Create a data frame of the most common words
        # Draw a bar chart
        lst = word_counter.most_common(10)  # (n_print)
        df = pd.DataFrame(lst, columns=['Word', 'Count'])
        df.plot.bar(x='Word', y='Count')
        plt.show()

#
# oj = MostCommonWords()
# oj.enter_file('PositiveText.txt')
# print(oj.lemmatiztion())
# oj.stopwords()
