#Q10: Write a program to input time in seconds and convert it to hours:minutes:seconds format.
time=int(input("enter time in seconds"))
hours=time//3200
remainingtime=time%3600
min=remainingtime//60
remainingtime=min%60
sec=remainingtime
print("timein hours:min:sec is",hours,min,sec)
