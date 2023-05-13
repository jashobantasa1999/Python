def fibo(a=10,b=50):
    pcheck =0
    print(a,b)
    n=0
    n1=1
    f =[]
    for i in range(10,50):
        n2 = n+n1
       
      
        for j in range (1,n2+1):
            print(j)
            if(n2%j==0):
                pcheck = pcheck+1
               
        if(pcheck==1):
            f.append(n2)
        n=n1
        n1=n2
        pcheck =0

    print("The prime fibo is: ")
    for i in f:
        if(i>=a and i<b):
            print(i)

c= int(input("enter 1 = requied argument ,2= key word argument ,3 = defult arrgument"))
if(c==1):
    a1 = int(input("enter a number"))
    b1 = int(input("enter a number"))
    fibo(a1,b1)
elif c ==2:
    a1 = int(input("enter a number"))
    b1 = int(input("enter a number"))
    fibo(a=a1,b=b1)
else:
    fibo()

