import numpy as np
a=np.array([[1,2],[3,5]])
b=np.array([[1],[2]])
inv=np.linalg.inv(a)
print("soln is ",inv.dot(b))