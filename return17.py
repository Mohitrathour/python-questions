def sum(x,y):
    s1=0;s2=0
    while(x>0):
        temp=x%10
        s1=s1+temp
        x=x//10
    while(y>0):
        temp1=y%10
        s2=s2+temp1
        y=y//10
    return s1,s2
x=int(input("enter no 1"))
y=int(input("enter no 2"))
a,b=sum(x,y)
print("sum of first no is",a)
print("sum of second no is",b)
        
