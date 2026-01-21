#Q13: Write a program to input a year and check whether it is a leap year or not using conditional statements.
n=int(input("enter a year to check"))
if(n%400==0 or n%100!=0 and n%4==0):
    print("its a leap year")
else:
    print("its not a leap year")
