#II. x-x3/3! + x5/5!-x7/7!+------+xn/n!

x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))
value=x
count=1
for i in range(3,n+1,2):
     xToPower = 1;
     factvalue = 1;
     for j in range(1,i+1):
        factvalue *= j
        xToPower *= x
            
     calculation = xToPower / factvalue
     if (count%2==0):
        value=value + calculation
     else:
       value=value - calculation
     count=count+1
print(value)