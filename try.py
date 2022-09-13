import matplotlib.pyplot as plt
import pandas as pd
import datetime


header=["temp","pressure","humidity","gas","altitude"]
df = pd.read_csv('data_cap/interior_bme688.csv', names=header)


date = str(datetime.datetime.now())
plt.figure(figsize=(9, 3))
plt.suptitle('run on: ' + date)

plt.subplot(131)
plt.plot(df[['humidity']])

plt.subplot(132)
plt.plot(df[['temp']])

plt.subplot(133)
plt.plot(df[['gas']])

plt.savefig("data.png", format="png")