import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use("ggplot")
templog = input("Temdata file\n")
y,x = np.loadtxt(templog + ".csv",
                 unpack=True, delimiter=",")

plt.plot(x,y)


plt.title("Temperature data")
plt.ylabel("Temp")
plt.xlabel("Time")


plt.show()

