def reverse(a):
    temp=0
    rev=0
    while(a>0):
      temp=a%10
      rev=rev*10+temp
      a=a//10
    return (rev)
a=int(input("enter the no "))
b=reverse(a)
print("reverse of the no:",b)
