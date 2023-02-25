#V. Difference between average of all even digits except divisible by
# 4 and avearge of all odd digits except divisble by 3 
n=int(input('Enter a number-'))
es,ec=0,0
os,oc=0,0
while n>0:
    r=n%10
    if (r%2==0 and r%4!=0):
         es=es+r
         ec=ec+1
    elif (r%2!=0 and r%3!=0):
        os=os+r
        oc=oc+1
    n=n//10
if(oc==0):
    oc=1
elif(ec==0):
    ec=1
oa=os/oc
ea=es/ec

if (ea>oa):
    diff=ea-oa
else:
    diff=oa-ea
print(diff)