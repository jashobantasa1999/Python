#Write a Python program to print and store ‘n terms of Fibonacci series in list
a =  int(input("enter a nth term"))
l=[0]
n,n1 =0,1
if(a>0):
    for i in range(a+1):
        b = n+n1
        l.append(b)
        n= n1
        n1 =b

print(l)
