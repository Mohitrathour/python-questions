#Q7: Write a program to swap two numbers without using a third variable.
n=int(input("enter no 1"))
m=int(input("enter no 2"))
n=n+m
m=n-m
n=n-m
print("swapped value of first value is:",n)
print("swapped value of second value is:",m)
