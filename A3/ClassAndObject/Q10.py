# wap to generate prime numbers in between 10 to 50 and 
# store it in list ,find avg of all prime number in the list ,check for 
# palindrome numbers available in the list and store in another 
# list,Display no of elements with elements in prime list and also 
# display no of elements with elements in palindrome list using 
# multiple inheritance


class Prime:
  
    l =[]
    def P(self):
        count = 0
        for i in range(10,51):
            for j in range(2,i):
                if(i%j==0):
                    count = count +1
            if(count ==0):    
                self.l.append(i)
            count=0
        print(self.l)

class Avg(Prime):
    sum =0
    def Avgs(self):
        for i in self.l:
            self.sum = self.sum+i
        print(self.sum)

class Palendrom(Prime):
    p =[]
    def isPalindrome(self) :
        for num in self.l:
            temp = num
            result = 0
            while(temp != 0) :
                rem = temp % 10

                result =  result * 10 + rem

                temp //= 10
            if num == result :
               self.p.append(num)
        print (self.p)

class Test(Avg,Palendrom):
    def __init__(self):
        print("Welcome")

a= Test()
a.P()
a.Avgs()
a.isPalindrome()
