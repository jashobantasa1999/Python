import math

def AreaPer(c,l,b=0,h=0):
    print(c,l,b,h)
    if(c==1):
        print("area of rectangle ",l*b)
        print("perimeter of rectangle  =",2*(l+b))
    elif c==2:
        print("area of square ",l*l)
        print("perimeter of square  =",(4*l))
    elif c==3:
        print("perimeter of trangle  =",(l+b+h))
        s = (l+b+h)//2
        area = math.sqrt(s*(s-l)*(s-b)*(s-h))
        print("area of trangle ",area)

c= int(input(" 1 for rectangle , 2 for square 3 for trangle"))

if(c==1):
    a = int(input("enter a side of "))
    b = int(input("enter a side of "))
    AreaPer(c,a,b)

elif(c==2):
    a = int(input("enter a side of "))
 
    AreaPer(c,a)

if(c==3):
    a = int(input("enter a side of "))
    b = int(input("enter a side of "))
    e = int(input("enter a side of "))
    AreaPer(c,a,b,e)
        


