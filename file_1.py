# this is a sample python file and so much code is not expected over here
import matplotlib.pyplot as plt
import random as ran
import numpy as np

n=int(input())
x,y=[],[]
for i in range(n):
  x.append(ran.randint(100))
  y.append(i+1)

x.y= np.array(x),np.array(y)
plt.scatter(x,y)
# plt.plot(x,y)
plt.show()
