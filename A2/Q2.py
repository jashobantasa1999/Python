import math
def Am(a =121):
   b = str(a)
   sum = 0
   for i in b:
        n  = math.pow(int(i),len(b))
        sum = sum + n
   if a ==sum :
       print("yes")
   else:
       print("no")
       


c= int(input("enter 1 = requied argument ,2= key word argument ,3 = defult arrgument"))
if(c==1):
    a1 = int(input("enter a number"))
    Am(a1)
elif c ==2:
    a1 = int(input("enter a number"))
    
    Am(a=a1)
else:
    Am()

