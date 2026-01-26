l=[16,56,23,45,15,16,17,2,1,89,56,7]
sumeven=0;sumodd=0;even=0;odd=0
for i in range(0,len(l)):
    if(l[i]%2==0):
        sumeven=sumeven+l[i]
        even+=1
    else:
        sumodd=sumodd+l[i]
        odd+=1
avgeven=sumeven/even
avrodd=smodd/odd
print("average of even digits:",avgeven)
print("average of odd digits:",avgodd)
