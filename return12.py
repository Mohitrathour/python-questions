def largest(a,b):
    if(a>b):
        return (a)
    else:
        return (b)
print("enter 10 no")
b=0
for i in range(1,11):
    n=int(input("enter no"))
    b=largest(b,n)
print("largest",b)    
    
