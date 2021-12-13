import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

class Comparison:

    @classmethod
    def comparison(cls):
        data = pd.read_excel('UCTLatest.xlsx', index_col=0)
        data2 = pd.read_excel('LAM.xlsx', index_col=0)
        data3 = pd.read_excel('AMAT.xlsx', index_col=0)

        Y = data['polarity']
        X = data['datetime']

        X2 = data2['datetime']
        Y2 = data2['polarity']

        X3 = data3['datetime']
        Y3 = data3['polarity']

        labl = ['Ultra Clean technology', 'Lam Research Corporation', 'Applied Materials, Inc']

        plt.plot(X, Y, label='Ultra Clean technology')
        plt.plot(X2, Y2, label='Lam Research Corporation')
        plt.plot(X3, Y3, label='Applied Materials, Inc')
        plt.title(label="Polarity Score of UCT, LAM and AMAT (2018 - 2021)",
                  fontsize=24,
                  color="black")
        plt.legend()

        plt.xticks(rotation=35)
        # plt.scatter(Y,X)
        plt.show()

        # import seaborn as sns
        # sns.displot(data['polarity'], bins=10, kde=True)
        # plt.show()




