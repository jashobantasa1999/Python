# b) capitalize first and last character of each word in string
a = input("enter a string")
b = a.split()
l=[]

for i in b:
    x= i[0].upper()+i[1:-1]+i[-1].upper()
    l.append(x)

l=" ".join(l)
print(l)
