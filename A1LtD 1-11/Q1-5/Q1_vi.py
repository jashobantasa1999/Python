# VI. Find kth digit from frontside or back side of any digits number 
# and find its poistional value
n=int(input('Enter a number-'))
p=int(input('Enter position number-'))
t=p-1
r=0
while p>0:
    r=n%10
    n=n//10
    p=p-1
while t>0:
    r=r*10
    t=t-1
print(r)