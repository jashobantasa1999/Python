# e) create a list to store unique character in string and another list 
# to store frequency of repeatation of unique character available in first list in the 
# string
a = input("enter a string  ")
c =[]
e=[]
d=[]
ind =0
for i in a:
    c.append(a.count(a[ind]))
    print(a[ind],c[ind])
    ind=ind+1
    if i not in d:
        d.append(i)
# print(c)
print(d)
for i in d:
    k = a.find(i)
    e.append(c[k])
print(e)
    



