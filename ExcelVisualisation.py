import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('report.xlsx', index_col=0)
print(data['polarity'])
dt = data['polarity'].value_counts()

import seaborn as sns
sns.displot(data['polarity'], bins=10, kde=True)
plt.show()

