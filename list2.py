l=[178,678,345,90,367,98,55,467,873,278,90]
s=0
for i in range(0,len(l)):
    if(l[i]>=100 and l[i]<=999 and l[i]%2!=0):
        s=s+l[i]
print("sum of all the three digit odd no is",s)
