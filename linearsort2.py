a=[]
print("enter 10 no")
for i in range(0,10):
    n=int(input("enter no"))
    a.append(n)
temp=0
for i in range(0,len(a)-1):
    if(a[i]<a[j]):
        temp=a[i]
        a[i]=a[j]
        a[j]=temp
print("after sorting")
for i in range(0,10):
    print(a[i])
