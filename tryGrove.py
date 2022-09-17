import matplotlib.pyplot as plt
import pandas as pd
import datetime

header=["temp","timestamp"]
df = pd.read_csv("data_cap/basement_bme_1.csv", names=header)

dfTimestamp = df['timestamp']
dfTemp = df['temp']

lTemperature = dfTemp.tolist()
lDates = dfTimestamp.tolist()
plt.figure(figsize=(25, 5))
plt.plot(lDates,lTemperature)
date = str(datetime.datetime.now().date())
plt.title = "Temp Last Run at " + date

plt.savefig("base_1.png", format="png")
