"""5. Write a python program compute following series and take a numbers num 
as inputx-x3/3! + x5/5!-x7/7!+------+xn/n!
 where x=sum of all even digits except 2 and 8
 and n= sum of all odd digits except 1 and 3"""
num = int(input("Enter the value of x:"))
count=0
x,n=0,0
while (num >0):
    t=num%10
    if (t%2==0):
        if (t!=2 and t!=8):
            x += t
    else:
        if (t!=1 and t!=3):
            n += t
    num=num//10 
print(x,n)
result=x
for i in range(3,int(n+1),2):
     xToPower = 1;
     factvalue = 1;
     for j in range(1,i+1):
        factvalue *= j
        xToPower *= x
            
     calculation = xToPower / factvalue
     if(count%2==0):
        result=result + calculation
     else:
        result=result - calculation
     count=count+1
print(result)