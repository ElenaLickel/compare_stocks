from matplotlib import pylab as plt
import pandas as pd

df_ko = pd.read_csv('KO.csv')
df_ko['Date'] = pd.to_datetime(df_ko.Date)
print(df_ko.head())
df_pep = pd.read_csv('PEP.csv')
df_pep['Date'] = pd.to_datetime(df_pep.Date)
print(df_pep.head())

index2 = []
for date2 in df_pep.Date:
    if df_ko.index[df_ko.Date == date2].values.size:
        index2.append(int(df_ko.index[df_ko.Date == date2].values[0]))
print(index2)

mean = df_ko["Close"].mean()

plt.figure('Coca Cola Stock vs Pepsi Stock')
plt.plot(df_ko['Date'],df_ko['Close'], linewidth=0.8, color = 'r', label = 'Coca Cola Stock')
plt.plot(df_pep['Date'],df_pep['Close'], linewidth=0.8, color = 'b',label = 'Pepsi Stock' )

plt.xlabel('Dates')
plt.ylabel('Stock Price')
plt.legend()


plt.show()

