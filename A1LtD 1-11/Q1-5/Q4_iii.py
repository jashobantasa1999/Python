#II. 1+x2/2! + x4/4!+x6/6!+------+xn/n!
x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))
value=x
for i in range(2,n+1,2):
     xToPower = 1;
     factvalue = 1;
     for j in range(1,i+1):
        factvalue *= j
        xToPower *= x
            
     calculation = xToPower / factvalue
     value=value + calculation
     
print(value)