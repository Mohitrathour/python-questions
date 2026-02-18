def names(a):
    b=[]
    for w in i:
        if(w[0]=='a' or w[0]=='A'):
            b.append(w)
    return b
a=[]
for i in range(0,20):
    n=input(" ")
    a.append(n)
x=names(a)
print(x)
