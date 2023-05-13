# Wap to compute factorial,GCD,LCM,sqrt without using any library
# function,swap two number without using 3rd variable using function and
# module?
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def Gcd(a,b):
     if(b == 0):
        return abs(a)
     else:
        return Gcd(b, a % b)
     
def Lcm(x, y):

  
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


def swap(a, b):
    a, b = b, a
    return a, b
