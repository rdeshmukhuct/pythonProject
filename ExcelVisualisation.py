import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('report.xlsx', index_col=0)


X = data['polarity']
Y = data['datetime']
plt.xticks(rotation = 35)
plt.scatter(Y,X)
plt.show()

import seaborn as sns
sns.displot(data['polarity'], bins=10, kde=True)
plt.show()



