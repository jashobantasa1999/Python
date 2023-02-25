"""2. Write a python program to find sum of product of corresponding digits of two 
any digit number Such as n=1234 m=7896 output=6*4+9*3+8*2+7*1"""
n=int(input('Enter 1st number-'))
n1=int(input('Enter 2nd number-'))
s=0
while n>0:
    r=n%10   
    r1=n1%10   
    p=r*r1
    s=s+p
    n=n//10
    n1=n1//10
print(s)