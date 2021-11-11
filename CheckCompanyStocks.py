import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

stocks = [{'ticker': 'UCTT',
           'name': 'Ultra Clean Technology'
    },
    {
        'ticker': 'LRCX',
        'name': 'Lam Research Corporation'
    },
    {
        'ticker': 'AMAT',
        'name': 'Applied Materials, Inc'
    }]

def create_plot(stocks):
    # Create an empty dataframe
    data = pd.DataFrame()
    for stock in stocks:
        # Create a column for the adjusted close of each stock
        # Here we use the DataReader library to get the data.
        data[stock['ticker']] = web.DataReader(stock['ticker'], data_source='yahoo', start='2007-1-1')['Adj Close']

    returns = data.apply(lambda x: (x / x[0] * 100))

    plt.figure(figsize=(10,6))

# Plot the returns
    for stock in stocks:
        plt.plot(returns[stock['ticker']], label=stock['name'])

# We need to call .legend() to show the legend.
    plt.legend()
# Give the axes labels
    plt.ylabel('Cumulative Returns %')
    plt.xlabel('Time')
    plt.show()

create_plot(stocks)