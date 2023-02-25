"""3. Write a python program to find sum of product of corresponding even digits 
of first any digit number and corresponding odd digit of any digit number 
Such as n=1234 m=4567 output=4*7+2*5
"""
n=int(input('Enter 1st number-'))
n1=int(input('Enter 2nd number-'))
s=0
while n>0:
    r=n%10   
    r1=n1%10 
    if (r%2==0): 
       p=r*r1
       s=s+p
    n=n//10
    n1=n1//10
print(s)