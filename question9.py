#Q9: Write a program to calculate simple and compound interest for given principal, rate, and time.
principal=int(input("enter principal"))
rate=int(input("enter rate"))
time=int(input("enter time"))
simple=(principal*rate*time)/100
compound=principal*((1+rate/100)**time)-principal
print("the simple interest is:",simple)
print("the compound interest is:",compound)
