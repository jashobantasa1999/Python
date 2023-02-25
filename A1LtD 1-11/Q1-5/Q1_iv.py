#iv. Sum of all prime digits
n=int(input('Enter a number-'))
s=0
while n>0:
    r=n%10
    if (r==2 or  r==5 or r==7 or  r==3):
          s=s+r
    n=n//10
print(s)