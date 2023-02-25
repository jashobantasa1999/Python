# f) find and count number of words starts and ends with vowels in a
# string of multiple words
a = input("enter a string   ")
c=[]
v=('a','e','i','o','u')
a = a.split()
for i in a:
    if(i.startswith(v) and i.endswith(v)):
        if i not in c:
            c.append(i)


    
for i in c:
    x = a.count(i)
    print(i,x)
 

