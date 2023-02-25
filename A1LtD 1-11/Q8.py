# 8. Write a python program to find 1st,2nd and 3rd largest and smallest numbers in
# a list 20 user defined values
l = []
for i in range(6):
    l.append(int(input("Enter a no")))
l.sort()
print("Smallest",l[0:3])
print("largest",l[-3:])
