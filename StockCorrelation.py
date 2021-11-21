import csv
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit

uct_date = []
uct_polarity = []

amat_date = []
amat_polarity = []

lam_date = []
lam_polarity = []

with open('UCTLatest.csv', 'r', encoding='utf-8') as read_csv:
    csv_reader = csv.DictReader(read_csv)

    for line in csv_reader:
        uct_date.append(line['datetime'])
        uct_polarity.append(line['polarity'])

with open('AMAT.csv', 'r', encoding='utf-8') as read_csv:
    csv_reader = csv.DictReader(read_csv)

    for line in csv_reader:
        amat_date.append(line['datetime'])
        amat_polarity.append(line['polarity'])

with open('LAM.csv', 'r', encoding='utf-8') as read_csv:
    csv_reader = csv.DictReader(read_csv)

    for line in csv_reader:
        lam_date.append(line['datetime'])
        lam_polarity.append(line['polarity'])

# uct_polarity = uct_polarity[:60]

lam_polarity = lam_polarity[:67]

lam_polarity = [float(i) for i in lam_polarity]
uct_polarity = [float(i) for i in uct_polarity]

print(len(uct_polarity))
print(len(amat_polarity))
print(len(lam_polarity))

print(pearsonr(uct_polarity, lam_polarity))

plt.scatter(lam_polarity, uct_polarity)

# b, m = polyfit(lam_polarity, uct_polarity, 1)
X_plot = np.linspace(0, 1, 5)
plt.plot(X_plot, X_plot* .15 + .10)
# plt.plot(lam_polarity, b + m * lam_polarity, '-')
plt.show()

## omit the first