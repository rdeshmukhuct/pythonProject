import collections
import inline as inline
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

file = open('NewFile.txt', encoding="utf8")
a = file.read()

stopwords = set(line.strip() for line in open('stopwords.txt'))
stopwords = stopwords.union(set(['uct', 'uctt', 'Up']))

wordcount = {}

for word in a.lower().split():
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace(":", "")
    word = word.replace("\"", "")
    word = word.replace("!", "")
    word = word.replace("*", "")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(20):
    print(word, ":", count)

file.close()
