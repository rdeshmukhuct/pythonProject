import datetime as dt
from tkinter import *

from tkcalendar import DateEntry

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas_datareader as web
from mplfinance.original_flavor import candlestick_ochl


class stockPrices:

    @classmethod
    def visualize(cls):
        def vs():
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
            ax.tick_params(axis='x', rotation=30, colors='white')
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

        btn_visualize = Button(root, text="Market Stock", font='Roboto', command=vs)
        btn_visualize.pack()


        root.mainloop()







