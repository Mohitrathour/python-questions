#Q18: Write a program that accepts a percentage (0-100) and assigns a grade based on the following criteria: 
a=int(input("enter the grade"))
if(a>=90 and a<=100):
    print("Grade A")
elif(a>=80 and a<=89):
    print("Grade B")
elif(a>=70 and a<=79):
    print("Grade C")
elif(a>=60 and a<=69):
    print("Grade D")
elif(a>=0 and a<=59):
    print("Grade F")
else:
    print("enter the valid marks")
