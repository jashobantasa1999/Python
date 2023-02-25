#IV. x-x3/3! + x5/5!-x7/7!+x11/11!------+xn/n!
x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))
value=x
count=1
for i in range(3,n+1):
     isNotPrime = False
     xToPower = 1
     factvalue = 1
     for j in range(1,i+1):
        if (j != 1 and j != i and i % j == 0):
           isNotPrime = True;
        factvalue *= j
        xToPower *= x
     if (isNotPrime):
        count=count+1
        continue;       
     calculation = xToPower / factvalue
     if (count%2==0):
        value=value + calculation
     else:
       value=value - calculation
     count=count+1
print(value)