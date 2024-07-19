import numpy as np
import matplotlib.pyplot as  plt
from  scipy.integrate import quad,trapz,simps
def f(x):
    return 4*x**2+3
x=np.arange(-5,5,0.01)
plt.plot(x,f(x))    
    
    
    