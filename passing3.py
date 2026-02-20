def check(a,b,c):
    if(a%10==9 and b%10==9 and c%10==9):
        print("all no ends withs 9")
    else:
        print("all no do not ends with 9")
a=int(input("enter the first no"))
b=int(input("enter the second no"))
c=int(input("enter the third no"))
check(a,b,c)
