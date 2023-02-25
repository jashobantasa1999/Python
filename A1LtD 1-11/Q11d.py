# d) Find the letter used maximum and minimum time in a string
a = input("enter a string  ")
c =[];
ind =0
for i in a:
    c.append(a.count(a[ind]))
    print(a[ind],c[ind])
    ind=ind+1
pos = c.index(max(c))
print("Max",a[pos])
pos = c.index(min(c))
print("Min",a[pos])

