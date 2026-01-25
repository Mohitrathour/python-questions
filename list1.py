#lists
l=[10,20,30,29,48,29,10,28,96,78,56]
s=0
for i in range(0,len(l)):
    if(l[i]%2==0):
        print(l[i])
        s=s+l[i]
print("sum of all even no is",s)        
