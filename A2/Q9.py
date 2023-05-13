swap=lambda a:a

a  = int(input("enter 1st no"))
b  = int(input("enter 2nd no"))
print(a,b)
c =b
b= swap(a)
a= swap(c)

print(a,b)