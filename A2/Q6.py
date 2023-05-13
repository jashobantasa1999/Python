def factargu(f):
    fact =1
    while f>0:
        fact = fact*f
        f= f-1
    print("factorial is",fact)

a=int(input("Enter a number"))
b = int(input(" 1 for for loop, 2 for while loop , 3 for do while loop ,4 for key word arguent "))

if(b==1):
    fact = 1
    for i in range(1,a+1):
        fact = fact*i
    print("factorial is",fact)
elif(b==2):
    fact =1
    c =a
    while(c>0):
        fact = fact*c
        c= c-1
    print("factorial is",fact)

elif(b==3):
    fact =1
    c=a
    while True:
        fact = fact*c
        c=c-1
        if(c==1):
            break
    print("factorial is",fact)
else:
    factargu(f=a)

    