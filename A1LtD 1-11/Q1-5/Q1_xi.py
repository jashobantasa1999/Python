"""XI. Difference between Sum of product of consecutive even digits 
except 2 and 6 and Sum of product of consecutive odd digits 
except 3 and 7 of any digit number"""
n=int(input('Enter a number-'))
es,os=0,0
p,p1=0,0
while n>0:
    r=n%10
    n=n//10    
    r1=n%10
    if ((r%2==0 and r!=2 and r!=6 and r1%2==0 and r1!=2 and r1!=6)):
        p=r*r1
        es=es+p
    elif ((r%2!=0 and r!=3 and r!=7 and r1%2!=0 and r1!=3 and r1!=7)):
        p1=r*r1
        os=os+p1
if(os>es):  
   print(os-es)
else:
    print(es-os)