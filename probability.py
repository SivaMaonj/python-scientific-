import random as rd
n=[10,100,500,1000,5000,10000,50000]
er_l=[]
for j in n:
    H=0
    T=0
    for i in range(j):
        toss=rd.randint(0,1)
        if toss==0:
            T=T+1
        else:
            H=H+1
    pH=H/j
    e=abs(0.5-pH)
    print(e)
    er_l.append(round(e,3))
print(er_l)    