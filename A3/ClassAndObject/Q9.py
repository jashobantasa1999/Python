# Wap to findout area and perimeter of rectangle and square using 
# method overriding and abstract class ?
from abc import ABC 
class Shape(ABC):
    def area(self):
        pass
    def perimeter(self):
        pass

class Rect(Shape):
    def __init__(self,a,b):
        self.l,self.b=a,b

    def area(self):
            print(" rectangle Area = ",self.l*self.b)        
    def  perimeter(self):
            print("rectangle perimeter = ",(self.l+self.b)*2)
                    
class Square(Shape):
    def __init__(self,a):
        self.l=a

    def area(self):
            print("square Area = ",self.l*self.l)        
    def  perimeter(self):
            print("square perimeter = ",(self.l+self.l)*2)

r  = Rect(4,5)
r.area()
r.perimeter()

s =Square(4)
s.area()
s.perimeter()