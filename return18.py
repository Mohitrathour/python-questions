def seperate(n):
    se=0
    so=0
    while(n>0):
        temp=n%10
        if(temp%2==0):
            se=se+temp
        else:
            so=so+temp
        n=n//10    
    return(se,so)
n=int(input("enter a no"))
se,so=seperate(n)
print("sum of even digits are:",se)
print("sum of odd digits are:",so)
