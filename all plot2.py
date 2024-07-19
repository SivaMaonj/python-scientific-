import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,.01)

def der(sci,x):
    y1=np.gradient(sci,x)
    y2=np.gradient(y1,x)

a=np.sin(x)
b=np.cos(x)
c=np.sinh(x)
d=np.cosh(x)

a1,a2=der(a,0.01)
b1,b2=der(b,0.01)
c1,c2=der(c,0.01)
d1,d2=der(d,0.01)

plt.subplot(2,2,1)
plt.plot(x,a)
plt.plot(x,a1)
plt.plot(x,a2)
plt.title("sin function")
plt.xlabel("x values")
plt.ylabel("sine x")
plt.grid()
plt.legend(["sin gfu","der1sin","der2 sdin"])

plt.subplot(2,2,2)
plt.plot(x,b)
plt.plot(x,b1)
plt.plot(x,b2)
plt.title("cosine function")
plt.xlabel("x values")
plt.ylabel("cos x")
plt.grid()
plt.legend(["cos gfu","der1cos","der2 cos"])

plt.subplot(2,2,3)
plt.plot(x,c)
plt.plot(x,c1)
plt.plot(x,c2)
plt.title("sinh function")
plt.xlabel("x values")
plt.ylabel("sinh x")
plt.grid()
plt.legend(["sinh gfu","der1sinh","der2 sinh"])

plt.subplot(2,2,4)
plt.plot(x,d)
plt.plot(x,d1)
plt.plot(x,d2)
plt.title("cosh function")
plt.xlabel("x values")
plt.ylabel("cosh x")
plt.grid()
plt.legend(["cosh gfu","der1cosh","der2 cosh"])s