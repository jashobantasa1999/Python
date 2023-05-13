# Wap to findout area and perimeter of a triangle having three sides
# using class?
import math
class Test:
    a=b=c=0
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c= c
    
    def area(self):
        s = (self.a+self.b+self.c)/2
        area = math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c)) 
        print("area of triangle is ",area)
    def perimeter(self):
        p = self.a+self.b+self.c
        print("perimeter is ",p)

obj =  Test(5,6,7)
obj.area()
obj.perimeter()