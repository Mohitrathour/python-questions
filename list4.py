def fattrick():
    l=[168,25,22,12,4,25,2,15,8,3,1,8,6,25]
    print("reverse order of list is:",l[ : :-1])
def loop():
    l=[168,25,22,12,4,25,2,15,8,3,1,8,6,25]
    for i in range(len(l)-1,-1,-1):
        print(l[i])
    return l
print(loop())
#print(fattrick())
