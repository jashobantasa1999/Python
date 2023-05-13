import os
f = open("number.txt",'w')

for i in range(3):
    d = input("Enter a number:-")
    d = d+","
    f.write(d)

f.seek(0,2)
f = open("number.txt","r+")
c  = f.read()

print(c)
s = c.split(",")
b = s[0:-1]
maximum = int(max(b))
minimum=  int(min(b))

dif = maximum - minimum
fact = 1
for i in range(2,dif+1):
    fact = fact* i
f.seek(0,2)
f.write(" Fact  = "+str (fact))
f.close()

os.rename("number.txt","fact.txt")





