import matplotlib.pyplot as plt
import numpy as np
import datetime

x = np.arange(0, 100, 0.00001)
y = x*np.sin(2*3.14*x)
plt.plot(y)

date = str(datetime.datetime.now())
plt.title('last run on: ' + date)

plt.savefig("test.png", format="png")
plt.savefig("test.svg", format="svg")