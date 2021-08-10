import datetime as dt
from tkinter import *
from tkinter import ttk

import mplfinance
from newspaper import Article
from textblob import TextBlob
from tkcalendar import DateEntry

from article_sentiment import ArticleSentiment

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas_datareader as web
from mplfinance.original_flavor import candlestick_ochl
import numpy as np


def summarize():
    url = utext.get('1.0', "end").strip()

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    summary.config(state='normal')

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    summary.config(state='disabled')

    analysis = TextBlob(article.text)




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
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.xaxis_date()

    candlestick_ochl(ax, data.values, width=0.5, colorup='#00ff00')
    plt.show()


root = Tk()

root.title("Stonk Market version 1")

label_from = Label(root, text='From:')
label_from.pack()
cal_from = DateEntry(root, width=50, year=2020, month=1, day=1)
cal_from.pack(padx=10, pady=10)

label_to = Label(root, text="To:")
label_to.pack()
cal_to = DateEntry(root, width=50)
cal_to.pack(padx=10, pady=10)

label_ticker = Label(root, text="Ticker Symbol")
label_ticker.pack()
text_ticker = Entry(root)
text_ticker.pack()

ulabel = Label(root, text='URL')
ulabel.pack()

utext = Text(root, height=1, width=140)
utext.pack()

summary = Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

btn_visualize = Button(root, text="Market Stock", command=visualize)
btn_visualize.pack()

btn_summary = Button(root, text="Summarize", command=summarize)
btn_summary.pack()

root.mainloop()


