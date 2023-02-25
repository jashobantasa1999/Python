#X. Sum of product of consecutive prime digits of any digit number
n=int(input('Enter a number-'))
s=0
p=0
while n>0:
    r=n%10
    n=n//10    
    r1=n%10
    if ((r==2 or r==3 or r==5 or r==7)and (r1==2 or r1==3 or r1==5 or r1==7)):
        p=r*r1
        s=s+p
    
print(s)