#I. Sum of all digits of any numbers
n=int(input('Enter a number-'))
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print(str(s))