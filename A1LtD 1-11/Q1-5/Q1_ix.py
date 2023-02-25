#IX. Sum of product of consecutive odd digits of any digit number
n=int(input('Enter a number-'))
s=0
p=0
while n>0:
    r=n%10
    n=n//10    
    r1=n%10
    if (r%2!=0 and r1%2!=0):
        p=r*r1
        print(p)
        s=s+p
    
print(s)