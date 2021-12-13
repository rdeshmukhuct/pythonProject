import csv

import matplotlib.pyplot as plt
import pandas as pd

pd.options.mode.chained_assignment = None

from matplotlib.pylab import rcParams

rcParams['figure.figsize'] = 20, 10

from article_analysis import GUIFunctions as gui


def on_pick(event):
    artist = event.artist
    xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
    x, y = artist.get_xdata(), artist.get_ydata()
    ind = event.ind
    print('Pick between vertices {} and {}'.format(min(ind), max(ind) + 1))
    print('Data point:', x[ind[0]], y[ind[0]])
    print


def plot_by_month():
    # quarter = [1,2,3,4]
    # eps = [.81, .92, .99, 1.07]
    gui.visualize()


class TimeSeries:

    def __init__(self):
        self.polarityScore = []
        self.dates = []
        self.df = pd.read_csv('files/report.csv')

    def open_csv(self, csv_file):
        with open(csv_file, 'r', encoding='utf-8') as read_csv:
            csv_reader = csv.DictReader(read_csv)

            for line in csv_reader:
                self.dates.append(line['datetime'])
                self.polarityScore.append(line['polarity'])

    def plot_df(self):
        fig, ax = plt.subplots()
        tolerance = 10
        ax.plot(self.df.datetime, self.df.polarity, 'ro-', picker=tolerance)
        plt.xticks(rotation = 45)
        plt.title(label="Polarity Score of UCT over the years (2018 - 2021)",
                  fontsize=24,
                  color="blue")

        # plt.figure(figsize=(25, 12.5), dpi=50)  # This will be modified to automatically adjust to screensize
        # plt.plot(self.df.datetime, self.df.polarity, color='tab:red', picker=tolerance)
        # plt.plot(self.df.datetime, eps, color= 'tab:blue')
        # plt.gca().set(title="Polarity Time Series", xlabel="Date", ylabel="Polarity")

        fig.canvas.callbacks.connect('pick_event', on_pick)
        plt.show()

    def main(self):
        print(self.dates)
        print(self.polarityScore)



#
# df = pd.read_csv('UCTT.csv')
# df = df[['Date', 'Close']]
#
# df = df.astype({"Close": float})
# df["Date"] = pd.to_datetime(df.Date, format="%Y/%m/%d")
#
# df.index = df['Date']
#
# plt.plot(df["Close"], label='Close Price history')
# # plt.show()
#
# df = df.sort_index(ascending=True, axis=0)
# data = pd.DataFrame(index=range(0, len(df)), columns=['Date', 'Close'])
#
# for i in range(0, len(data)):
#     data["Date"][i] = df['Date'][i]
#     data["Close"][i] = df['Close'][i]
#
# scalar = MinMaxScaler(feature_range=(0, 1))
# x_train_data, y_train_data = [], []
# # x_train_data = np.asarray(x_train_data)
# # y_train_data = np.asarray(y_train_data)
# # x_train_data = np.reshape(x_train_data, x_train_data[0])
#
# data.index = data.Date
# data.drop("Date", axis=1, inplace=True)
#
# final_data = data.values
# train_data = final_data[0:200, :]
# valid_data = final_data[200:, :]
#
# scalar = MinMaxScaler(feature_range=(0, 1))
#
# scaled_data = scalar.fit_transform(final_data)
# # x_train_data, y_train_data = [], []
# # x_train_data = np.asarray(x_train_data)
# # y_train_data = np.asarray(y_train_data)
#
# for i in range(60, len(train_data)):
#     x_train_data.append(scaled_data[i - 60:i, 0])
#     y_train_data.append(scaled_data[i, 0])
#
# x_train_data = np.asarray(x_train_data)
# y_train_data = np.asarray(y_train_data)
# x_train_data = np.reshape(x_train_data, (x_train_data.shape[0], x_train_data.shape[1], 1))
#
# lstm_model = Sequential()
# lstm_model.add(LSTM(units=50, return_sequences=True, input_shape=(np.shape(x_train_data)[1], 1)))
# lstm_model.add(LSTM(units=50))
# lstm_model.add(Dense(1))
#
# model_data = data[len(data) - len(valid_data) - 60:].values
# model_data = model_data.reshape(-1, 1)
# model_data = scalar.transform(model_data)
#
# lstm_model.compile(loss='mean_squared_error', optimizer='adam')
# lstm_model.fit(x_train_data, y_train_data, epochs=1, batch_size=1, verbose=2)
#
# x_test = []
# for i in range(60, model_data.shape[0]):
#     x_test.append(model_data[i - 60:i, 0])
#
# x_test = np.array(x_test)
# x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
#
# predict_stonks_price = lstm_model.predict(x_test)
# predict_stonks_price = scalar.inverse_transform(predict_stonks_price)
#
# train_data = data[:200]
# valid_data = data[200:]
# valid_data["Predictions"] = predict_stonks_price
# plt.plot(train_data["Close"])
# plt.plot(valid_data[['Close', "Predictions"]])
# plt.show()

# Red is Actual
# Green is predicted

# print(data.head())
#
# print(df.dtypes)
#
# print(df.head())

#t = TimeSeries()
#t.open_csv('report.csv')
# t.plot_by_month()
#t.plot_df()
#t.main()
