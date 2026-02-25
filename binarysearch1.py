#binary search
#w.a.p to enter 10 no in a list in ascending order and search for a specific no
#with its position using binary sort technique if not found then print the message no not found
a=[]
print("enter 10 no")
for i in range(0,10):
    n=int(input("enter no"))
    a.append(n)
first=0
last=9
search=int(input("enter no to be searched"))
mid=(first+last)//2
while(first<=last):
    if(a[mid]<search):
        first=mid+1
    elif(a[mid]==search):
        print("number found at position=",(mid+1))
        break
    else:
        last=mid-1
    mid=(first+last)//2
if(first>last):
   print("no not found")

   
