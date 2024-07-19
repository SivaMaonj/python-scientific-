num=[]
print("enter size")
n=int(input())
print("enter element")
for i in range(0,n):
    num .insert(i,int(input()))
for i in range(0,n):
    for j in range(0,n-1):
        if num[j]>num[j+1]:    
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp
print("sorted list is" )
for i in range (0,n):
    print(num[i])           
