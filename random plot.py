import numpy as np
import matplotlib.pyplot as plt
x=np.random.uniform(1,10,10)
y=np.random.uniform(1,10,10)
plt.subplot(2,1,1)
plt.stem(x,y)
plt.xlabel("x value")
plt.ylabel("y value")
plt.title(' stem plot')