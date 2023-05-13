# WAP to find factorial,GCD,LCM ,generate prime numbers in 
# between user defined range, and generate febonacci series in 
# between user defined range using multiple inheritance?


from math import factorial
from math import gcd


class T1:
    d=[]
    m=1
    def __init__(self,a,b):
        self.a,self.b = a,b
        self.d.extend(range(self.a,self.b))
        print(self.d)
    def fact(self):
        for i in range(self.a,self.b):
            print(factorial(i))

class Prime:
  
    l =[]
    def __init__(self,a,b):
        self.a,self.b = a,b

    def P(self):
        count = 0
        for i in range(self.a,self.b):
            for j in range(2,i):
                if(i%j==0):
                    count = count +1
            if(count ==0):    
                self.l.append(i)
            count=0
        print(self.l)
class GCD(T1):

    def __init__(self):
        def solve(nums):
            if len(nums) == 1:
             return nums[0]

            div = gcd(nums[0], nums[1])

            if len(nums) == 2:
             return div

            for i in range(1, len(nums) - 1):
             div = gcd(div, nums[i + 1])
             if div == 1:
                 return div

             return div
        nums = self.d
        self.gcd = solve(nums)
        print("gcd = ",self.gcd)
        for i in self.d:
            self.m = self.m*i
        print("lcm = ",self.m//self.gcd)


     
t = T1(50,100)
g=GCD()