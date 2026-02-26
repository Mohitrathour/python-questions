a=[]
print("enter 10 no")
for i in range(0,10):
    n=int(input(" "))
    a.append(n)
temp=0
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("after linear sort")
for i in range(0,10):
    print(a[i])
    
