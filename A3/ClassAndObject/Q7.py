# Wap to findout volume of a box using simple inheritance ?
class Test:
    def volume(self,a,b,c):
        v= a*b*c
        print("The Volume is ",v)

class V(Test):
    pass

a= int(input("enter the length"))
b= int(input("enter the  breadth"))
c= int(input("enter the height"))

v =  V()
v.volume(a,b,c)