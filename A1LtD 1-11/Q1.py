# Write a python program to create a list of prime numbers as per given range
a = int(input("Enter the start no"))
b = int(input("Enter the end no"))
l = list(range(a,b))
pcheck =1
l1=[]
for i in l:
    for j in range(2,i):
        if(i%j==0):
            pcheck = pcheck+1
    if(pcheck==1):
        l1.append(i)
    pcheck =1   
print(l1)
