import matplotlib.pyplot as plt
import pandas as pd
import datetime

header=["temp","pressure","humidity","gas","altitude","timestamp"]
df = pd.read_csv('data_cap/interior_bme688.csv', names=header)

date = str(datetime.datetime.now())
plt.figure()
plt.suptitle('run on: ' + date)

arr = df.to_numpy()

#x = [0.00001,0.001,0.01,0.1,0.5,1,5]
arrList = arr.tolist()
x=arrList[0][0]
# create an index for each tick position
xi = list(range(len(x)))
y = arrList[0][5]
#y = [0.945,0.885,0.893,0.9,0.996,1.25,1.19]
#plt.ylim(0.8,1.4)
# plot the index for the x-values
plt.plot(xi, y, marker='o', linestyle='--', color='r', label='Square') 
plt.xlabel('Temp C')
plt.ylabel('Time') 
plt.xticks(xi, x)
plt.title('Temperature readings')
plt.legend() 
#plt.show()

plt.savefig("data3.png", format="png")
