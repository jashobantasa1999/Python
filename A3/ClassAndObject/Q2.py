# Wap to findout area and perimeter of a rectangle and square using
# class ?

# Wap to findout area and perimeter of a triangle having three sides
# using class?
import math
class Test:
    a=b=c=0
    def __init__(self,a):
        self.a = a
        area =self.a*self.a
        print("area of squar is ",area)
        p = self.a*4
        print("perimeter is ",p)
class Test1:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        area =self.a*self.b
        print("area of squar is ",area)
        p = (self.a+self.b)*2
        print("perimeter is ",p)
    
   

obj =  Test(5)
obj1 =  Test1(5,4)
