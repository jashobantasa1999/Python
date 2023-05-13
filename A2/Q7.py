def search(a,s):
    a.sort()
    b= a
    low = 0     
    high = len(a)

    for i in range(low,high+1):
        if b[(low+high)//2]==s:
            print(" index is ", (low+ high)//2)
            break
        elif(b[(low+high)//2]>s):
            high = (low+high)//2-1
        elif(b[(low+high)//2]<s):
            low = (low+high)//2+1

a =[]
for i in range (5):
    b=  int(input("enter a number "))
    a.append(b)
print(" your enter nos are ",a)
s = int (input(" enter which no you want to search"))
search(a,s)
