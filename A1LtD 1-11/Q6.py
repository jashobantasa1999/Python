# 6. Write a python program to store names of 10 fruits in strings and sort in
# alphabetical order
l=[]
for i in range(10):
    l.append(input("enter a fruit name"))

l.sort()
print(l)