num=[]
print("enter size")
n=int(input())
print("enter element")
for i in range(0,n):
    num .insert(i,int(input()))
print("enter element to search")
tosearch=int(input())
count=0
for i in range (0,n):
    if num[i]==tosearch:
        count=1
if count==1:
        print("element found")
else:
        print("not found")    