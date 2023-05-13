import  Q2module as q

b = int (input("enter the size of stack"))

a =[]
for i in range(b):  
    if(q.isfull(a,b)):
        break
    else:
        c = int (input("Enter a no"))
        q.push(a,c)

d = int (input("enter the no you want to search"))
q.peak(a,d)

for i in range(5):
   
    a = q.popelment(a)

print (a)


