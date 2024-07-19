import numpy as np
A=np.array([[1,2,3],[3,4,5],[5,6,7]])
print(A)
B=np.array([[1],[1],[1]])
print(B)
result=np.array([[0],[0],[0]])
print(A.dot(B))
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][k]*B[k][j]
            
for   r in result :
    print(r)  
print(len(B[0]))                    