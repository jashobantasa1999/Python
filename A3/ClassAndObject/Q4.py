# Wap to swap two numbers without using 3rd variable and with using
# 3rd variable using class?

class Test:
    def __init__(self,a,b):
        self.a,self.b=a,b

    def Swap(self):
        self.a = self.a+self.b
        self.b = self.a - self.b
        self.a = self.a - self.b
        print("a =",self.a,"b = ",self.b)

    def Swap1(self):
        temp = self.a
        self.a = self.b
        self.b = temp
        print("a =",self.a,"b = ",self.b)
    
obj = Test(5,6)

obj.Swap()
obj.Swap1()