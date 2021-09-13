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


# The main purpose of GUIFnctions() is to assist GUI.py when calling functions and to reduce class size
# It calls upon main.py

class GUIFunctions:
    print("You are in the article_analysis.py - GUIFunctions")
    ob = main.MostCommonWords()

    # search_articles(): takes zero arguments and return a list of parsed urls called urls as well as list[dict{}].
    # d1 and d2 are dates that the user can change to get different articles from different dates.
    # google_news.get_news('UCTT') and google_news.search('UCTT') both take in the ticker argument to scrape for the
    # specified data. The reason they arent passed as arguments in the class is because we don't want the users, to be
    # able to modify that data.
    @classmethod
    def search_articles(cls):
        start_date = '08/01/2021'  # Format must be MM/DD/YYYY, User can change
        end_date = '08/16/2021'  # Format must be MM//DD/YYYY, User can change
        google_news = GoogleNews()
        google_news.set_time_range(start_date, end_date)  # You can hard code the Dates here or at the top
        google_news.set_encode('utf-8')
        google_news.get_news('UCTT ham-let ltd ')  # This Can be changed to any Company Ticker
        google_news.search('UCTT ham-let ltd')  # Change this to the Company Ticker above
        links = google_news.get_links()
        result = google_news.result()
        google_news.clear()

        protocol = 'https://'  # appends the protocol if the url if the url is missing it.
        urls = [protocol + domain if protocol not in domain else domain for domain in links]
        return urls, result

    # visualize(): takes zero arguments and returns no data.
    # its primary task is to get the current stock price of the company.
    # for modifications of the time period and company ticker, you can modify
    # argument 1, 3, 4, but don't modify the second argument
    # data = web.DataReader('Company_Ticker', 'yahoo', 'Change_Start_Date', 'Change_End_Date')
    @classmethod
    def visualize(cls):
        # HAML ticker not found, so using UCTT for debugging purposes
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
        fig, (ax, ax1) = plt.subplots(1, 2, figsize=(10, 10))

        # bar graph to visualise data
        type_of_sentiment = ['Positive', 'Negative', 'Neutral']
        data = datalist
        rects = ax.bar(type_of_sentiment, data)
        ax.set_title("Sentiment Article Analysis of Scraped Data ")

        for rect, label in zip(rects, data):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')

        # Pie chart for data visualisation
        ax1.pie(datalist, labels=type_of_sentiment, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.set_title("Sentiment Article Analysis of Scraped Data ")

        plt.show()


        # type_of_sentiment = ['Positive', 'Negative', 'Neutral']
        # data = datalist
        # fig = plt.figure(figsize=(10, 7))
        # ax = plt.subplot()
        # wp = {'linewidth': 1, 'edgecolor': 'black'}
        # plt.pie(data, autopct=lambda length: self.get_article_length(length, data), labels=type_of_sentiment,
        #        wedgeprops=wp)
        # ax.set_title("Sentiment Article Analysis of Scraped Data ")
        # plt.show()

    @classmethod
    def get_article_length(cls, length, values):
        l = int(length / 100. * sum(values))
        return "{:d} Articles".format(l)

    # read_lines(): takes zero arguments, and returns the int value of string values for a text file.
    # refer to documentation above GUIFunction.pie_chart()
    @classmethod
    def read_lines(cls):
        len_of_articles_list = []
        file1 = open('data.txt', 'r')
        lines = file1.readlines()
        count = 0
        for line in lines:
            count += 1
            len_of_articles_list.append(line.strip())
        values = [int(i) for i in len_of_articles_list]
        return values
