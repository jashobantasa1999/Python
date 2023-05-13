import os
f = open("myself.txt","w")

d = input("enter some data  :- ")

f.write(d)
f= open("myself.txt","r+")
b = f.read()
g = open("backup.txt","w")
g.write(b)
g = open("backup.txt","r")
c= b[::-1]
f.seek(0)
f.write(c)
s1 = f.read()
s2 = g.read()
print(s1,s2)
if (s1.__eq__(s2)):
    print("its palendrom")
else:
    print("not palendrom")

g.close()
# os.remove("backup.txt")





