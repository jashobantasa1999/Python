""". Write a python program to compute following series and take input x and n
I. 1-x2/2! + x3/3!-x4/4!+------+xn/n!"""
value = 1
x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))
 
for i in range(2,n+1):
     xToPower = 1;
     factvalue = 1;
     for j in range(1,i+1):
        factvalue *= j
        xToPower *= x
            
     calculation = xToPower / factvalue
     if (i%2==0):
        value=value-calculation
     else:
       value=value + calculation
print(value)
 