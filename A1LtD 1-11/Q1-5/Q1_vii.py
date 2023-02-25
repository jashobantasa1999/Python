#VII. Sum of product of consecutive digits of any digit number
n=int(input('Enter a number-'))
s=0
while n>0:
    r=n%10
    n=n//10    
    r1=n%10
    p=r*r1
    s=s+p
    
print(s)