#Q15: Write a program to input a character and check whether it is an uppercase alphabet, lowercase alphabet, digit, or special character.

a=input("enter a character")
if(a>='A' and a<='Z'):
    print("the character is uppercase alphabet")
elif(a>='a' and a<='z'):
    print("the character is lowercase alphabet")
elif(a>=0 and a<=9):
    print("it is digit")
else:
    print("its a special character")
