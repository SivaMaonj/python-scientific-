import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,.01)

a=np.sin(x)
b=np.cos(x)
c=np.sinh(x)
d=np.cosh(x)

plt.subplot(2,2,1)
plt.plot(x,a)
plt.title("sin function")
plt.xlabel("x values")
plt.ylabel("sine x")
plt.grid()
plt.legend()

plt.subplot(2,2,2)
plt.plot(x,b)
plt.title("cosine function")
plt.xlabel("x values")
plt.ylabel("cos x")
plt.grid()
plt.legend()

plt.subplot(2,2,3)
plt.plot(x,c)
plt.title("sinh function")
plt.xlabel("x values")
plt.ylabel("sinh x")
plt.grid()
plt.legend()

plt.subplot(2,2,4)
plt.plot(x,d)
plt.title("cosh function")
plt.xlabel("x values")
plt.ylabel("cosh x")
plt.grid()
plt.legend()

