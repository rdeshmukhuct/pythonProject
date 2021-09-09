import sqlite3

from GoogleNews import GoogleNews
from mplfinance.original_flavor import candlestick_ochl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas_datareader as web
import numpy as np
import main

ob = main.MostCommonWords()
conn = sqlite3.connect('test.db')
c = conn.cursor()


# The main purpose of GUIFnctions() is to assistn GUI.py when calling functions and to reduce class size
# It calls upon main.py
class GUIFunctions():
    ob = main.MostCommonWords()

    # search_articles(): takes zero arguments and return a list of parsed urls called urls.
    # d1 and d2 are dates that the user can change to get different articles from different dates.
    # google_news.get_news('UCTT') and google_news.search('UCTT') both take in the ticker argument to scrape for the
    # specified data. The reason they arent passed as arguments in the class is because we don't want the users, to be
    # able to modify that data.
    def search_articles(self):
        d1 = '08/01/2021'
        d2 = '08/16/2021'

        google_news = GoogleNews()

        google_news.set_time_range(d1, d2)
        google_news.set_encode('utf-8')
        google_news.get_news('UCTT')
        google_news.search('UCTT')

        results = google_news.get_page()
        links = google_news.get_links()
        print("Append ", google_news.result())
        google_news.clear()
        protocol = 'https://'  # appends the protocol if the url if the url is missing it.
        # urls = np.array([protocol + domain if protocol not in domain else domain for domain in links])
        urls = [protocol + domain if protocol not in domain else domain for domain in links]
        for i in google_news.result():
            c.execute("INSERT INTO test VALUES (:title, :desc, :date, :datetime, :link, :img, :media, :site)", i)
        c.execute("SELECT * FROM test WHERE date='Aug 27'")
        print(c.fetchone())
        return urls

    # visualize(): takes zero arguments and returns no data.
    # its primary task is to get the current stock price of the company.
    # for modifications of the time period and company ticker, you can modify
    # argument 1, 3, 4, but don't modify the second argument
    # data = web.DataReader('Company_Ticker', 'yahoo', 'Change_Start_Date', 'Change_End_Date')
    def visualize(self):
        data = web.DataReader('UCTT', 'yahoo', '08/01/2021', '08/16/2021')
        data = data[['Open', 'High', 'Low', 'Close']]

        data.reset_index(inplace=True)
        data['Date'] = data['Date'].map(mdates.date2num)

        ax = plt.subplot()
        ax.grid(True)
        ax.set_axisbelow(True)
        ax.set_title('{} Share Price'.format('UCTT'), color='white')
        ax.figure.canvas.set_window_title("Alpha Version v0.1 Alpha")
        ax.set_facecolor('black')
        ax.figure.set_facecolor('#121212')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.xaxis_date()

        candlestick_ochl(ax, data.values, width=0.5, colorup='#00ff00')
        plt.show()

    # pie_chart(): takes zero arguments and returns nothing
    # takes data from GUIFunction.read_lines() which returns pre-processed data that gives the length of
    # negative, positive, and neutral sentiment articles that were pre computed in article_sentiment().
    # It displays a pie chart
    def pie_chart(self, datalist):
        l = ['Postive', 'Negative', 'Neutral']
        #data = self.read_lines()
        data = datalist
        fig = plt.figure(figsize=(10, 7))
        ax = plt.subplot()
        plt.pie(data, labels=l)
        ax.set_title("Sentiment Article Analysis of Scraped Data ")
        plt.show()

    # read_lines(): takes zero arguments, and returns the int value of string values for a text file.
    # refer to documentation above GUIFunction.pie_chart()
    def read_lines(self):
        list = []
        file1 = open('data.txt', 'r')
        lines = file1.readlines()
        count = 0
        for line in lines:
            count += 1
            list.append(line.strip())
        values = [int(i) for i in list]
        return values
