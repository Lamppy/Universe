import matplotlib.pyplot as plt
import pandas
import scipy

df1 = pandas.read_csv("Temperature.csv")
df1["Temperature"].plot(kind="bar")
plt.show()
df1["Temperature"].plot.kde()
plt.show()
print(scipy.stats.kstest(df1, 'norm', (df1.mean(), df1.std()), N=len(df1)))
