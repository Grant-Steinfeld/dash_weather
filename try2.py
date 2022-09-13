import matplotlib.pyplot as plt
import pandas as pd
import datetime

header=["temp","pressure","humidity","gas","altitude"]
df = pd.read_csv('data_cap/interior_bme688.csv', names=header)

date = str(datetime.datetime.now())
plt.figure()
plt.suptitle('run on: ' + date)

plt.subplot(221)
plt.plot(df[['temp']])

plt.subplot(222)
plt.plot(df[['pressure']])

plt.subplot(223)
plt.plot(df[['humidity']])

plt.subplot(224)
plt.plot(df[['gas']])


plt.savefig("data2.png", format="png")
