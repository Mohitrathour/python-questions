def new(a):
    l=[]
    for w in i:
        if(w[0]== w[-1]):
            l.append(w)
    return l
a=[]
for i in range(0,20):
    n=input(" ")
    a.append(n)
b=new(a)
print("list:",b)
            
