# 7. Write a python program to find difference between average of all even
# numbers except divisible by 4 and average of all odd numbers except
# divisible by 5 in a list of user defined 20 values?

l=[]
for i in range(4):
    l.append(int(input("enter a number")))
seven =0
ecount=0
sodd =0
ocount=0
for i in l:
    if(i%2==0 and i%4 !=0):
        seven= seven+ i
        ecount=ecount+1
    elif(i%2 !=0 and i%5!=0):
        sodd=sodd+i
        ocount=ocount+1

avg= seven/ecount - sodd/ocount
print(avg)
