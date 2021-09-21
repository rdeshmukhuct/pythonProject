import datetime as dt
from tkinter import *

from newspaper import Article
from textblob import TextBlob
from tkcalendar import DateEntry

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas_datareader as web
from mplfinance.original_flavor import candlestick_ochl

from GoogleNews import GoogleNews
import numpy as np


def summarize():
    ticker = text_ticker.get()
    from_date = cal_from.get_date()
    to_date = cal_to.get_date()

    d1 = from_date.strftime("%m/%d/%Y")
    d2 = to_date.strftime("%m/%d/%Y")

    print(d1)
    print(d2)

    google_news = GoogleNews()
    google_news.set_lang('en')
    google_news.set_time_range(start=d1, end=d2)
    google_news.set_encode('utf-8')
    ticker = ticker + "stock"    # Get news of the ticker stock and then summarize it
    google_news.get_news(ticker)
    google_news.search(ticker)
    results = google_news.result(sort=True)
    links = google_news.get_links()
    protocol = 'https://'  # appends the protocol if the url if the url is missing it.
    urls = np.array([protocol + domain if protocol not in domain else domain for domain in links])
    article = Article(urls[1])
    article.download()
    article.parse()
    article.nlp()

    summary.config(state='normal')

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    summary.config(state='disabled')

    analysis = TextBlob(article.text)


# def get_articles():
#     from_date = cal_from.get_date()
#     to_date = cal_to.get_date()
#
#     d1 = from_date.strftime("%m/%d/%Y")
#     d2 = to_date.strftime("%m/%d/%Y")
#
#     print(d1)
#     print(d2)
#
#     google_news = GoogleNews()
#     google_news.set_lang('en')
#     google_news.set_time_range(start=d1, end=d2)
#     google_news.set_encode('utf-8')
#     google_news.get_news('UCTT')
#     google_news.search('UCTT')
#     results = google_news.result(sort=True)
#
#     links = google_news.get_links()
#     google_news.clear()
#
#
#
#     # protocol = 'https://'
#     # url = np.array([protocol+domain if protocol not in domain else domain for domain in links])
#     # url = np.array([domain for domain in links])
#     summary_len.config(state='normal')
#
#     summary_len.delete('1.0', 'end')
#     summary_len.insert('1.0', [result['title'] for result in results])
#
#     summary_len.config(state='disabled')


def visualize():
    from_date = cal_from.get_date()
    to_date = cal_to.get_date()

    start = dt.datetime(from_date.year, from_date.month, from_date.day)
    end = dt.datetime(to_date.year, to_date.month, to_date.day)

    ticker = text_ticker.get()
    data = web.DataReader(ticker, 'yahoo', start, end)
    data = data[['Open', 'High', 'Low', 'Close']]

    data.reset_index(inplace=True)
    data['Date'] = data['Date'].map(mdates.date2num)

    ax = plt.subplot()
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_title('{} Share Price'.format(ticker), color='white')
    ax.figure.canvas.set_window_title("Alpha Version v0.1 Alpha")
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.tick_params(axis='x', rotation=30,  colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.xaxis_date()

    candlestick_ochl(ax, data.values, width=0.5, colorup='#00ff00')
    plt.show()


root = Tk()

root.title("Stock Market version 2")

label_from = Label(root, text='From:', font='Roboto')
label_from.pack()
cal_from = DateEntry(root, width=50, year=2020, month=1, day=1)
cal_from.pack(padx=10, pady=10)

label_to = Label(root, text="To:", font='Roboto')
label_to.pack()
cal_to = DateEntry(root, width=50)
cal_to.pack(padx=10, pady=10)

label_ticker = Label(root, text="Ticker Symbol", font='Roboto')
label_ticker.pack()
text_ticker = Entry(root)
text_ticker.pack()

ulabel = Label(root, text='URL', font='Roboto')
ulabel.pack()

utext = Text(root, height=1, width=100)
utext.pack()

summary = Text(root, height=20, width=100)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

# lenLabel = Label(root, text='Len', font='Roboto')
# lenLabel.pack()
#
# summary_len = Text(root, height=10, width=100)
# summary_len.config(state='disabled', bg='#dddddd')
# summary_len.pack()


btn_visualize = Button(root, text="Market Stock", font='Roboto', command=visualize)
btn_visualize.pack()

btn_summary = Button(root, text="Summarize", font='Roboto', command=summarize)
btn_summary.pack()

# btn_len = Button(root, text='Articles', font='Roboto', command=get_articles)
# btn_len.pack()

root.mainloop()
