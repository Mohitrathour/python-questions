#Q19: Write a program to classify a triangle as Equilateral, Isosceles, or Scalene based on its side lengths.
n1=int(input("enter no 1"))
n2=int(input("enter no 2"))
n3=int(input("enter no 3"))
if (a + b <= c) or (a + c <= b) or (b + c <= a):
            print("Invalid Triangle")
            return
if(n1==n2 and n2==n3 and n3==n1):
    print("isosceles")
elif(n1==n2==n3):
    print("equilateral")
else:
    print("scalene")
