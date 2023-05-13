# Wap to findout volume,cost and weight of a box using multilevel 
# inheritance with and without super keyword?

class Box:
    def __init__(self,a,b,c):
        self.ln,self.br,self.h =a,b,c

    def volume(self):
        self.v = self.ln*self.br*self.h
        print(" the volume is " ,self.v)
         
         


class Box1(Box):
    def __init__(self, a, b, c,w):
          self.ln,self.br,self.h,self.wt =a,b,c,w

    def Weight(self):
        self.w = self.v*self.wt
        print("Weight =" ,self.w)

class Box2(Box1):
    def __init__(self, a, b, c,w,p):
          self.ln,self.br,self.h,self.p,self.wt =a,b,c,p,w

    def cost(self):
         self.ct = self.p * self.w
         print("cost = ",self.ct)


b2 = Box2(1,2,3,5,10)
b2.volume()
b2.Weight()
b2.cost()
        

    