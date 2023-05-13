# 6. WAP to compute simple interest and compound interest for different
# banks like SBI,UBI, AXIS having individual rate of Interest using
# method overriding, multiple inheritence and abstract class.

from abc import ABC

class Interest(ABC):
    def SInterest(self):
        pass
    def CInterest(self):
        pass
class SBI(Interest):
    
    def __init__(self,p,t,r):
        self.p,self.t,self.r = p,t,r
    def SInterest(self):
        s = (self.p*self.t*self.r)/100
        print("SBI  SI " ,s)
    def CInterest(self):
        a= self.p*(1+self.r/100)**self.t
        i = a-self.p
        print("SBI CIntrest ",i)   
        
class UBI(Interest):
    
    def __init__(self,p,t,r):
        self.p,self.t,self.r = p,t,r
    def SInterest(self):
        s = (self.p*self.t*self.r)/100
        print("UBI  SI " ,s)
    def CInterest(self):
        a= self.p*(1+self.r/100)**self.t
        i = a-self.p
        print("UBI CIntrest ",i)   
class AXIS(Interest):
    
    def __init__(self,p,t,r):
        self.p,self.t,self.r = p,t,r
    def SInterest(self):
        s = (self.p*self.t*self.r)/100
        print("AXIS  SI " ,s)
    def CInterest(self):
        a= self.p*(1+self.r/100)**self.t
        i = a-self.p
        print("AXIS CIntrest ",i)   


p= int(input("enter the principal"))
t= int(input("enter the time"))
r1= int(input("enter the rate for SBI "))
r2= int(input("enter the rate for UBI "))
r3= int(input("enter the rate for  AXIS "))

s= SBI(p,t,r1)
U= UBI(p,t,r2)
A= AXIS(p,t,r3)

s.SInterest(),s.CInterest()
U.SInterest(),U.CInterest()
A.SInterest(),A.CInterest()
