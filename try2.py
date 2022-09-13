import matplotlib.pyplot as plt
import pandas as pd
import datetime

header=["humidity","temp","gas","pressure","timestamp"]
df = pd.read_csv('data_cap/study_bme_1.csv', names=header)

date = str(datetime.datetime.now())
plt.figure()
plt.suptitle('run on: ' + date)

plt.subplot(221)
plt.plot(df[['humidity']])

plt.subplot(222)
plt.plot(df[['temp']])

plt.subplot(223)
plt.plot(df[['gas']])

plt.savefig("data2.png", format="png")
