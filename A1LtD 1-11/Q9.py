# Write a python program to find repeated numbers as well as frequency of
# repetition of numbers in a list of 20 user defined values?

l =[]
for i in range(5):
    l.append(int(input("enter item in list:-")))
u=set(l)
f=[]
for i in u:
    a=l.count(i)
    f.append(a)
print("Given int",l)
print("unique item:",u)
print("frequency:-",f)


    

