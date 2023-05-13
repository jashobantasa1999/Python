def Biodata(name, *value):
    print ("name:=",name)
    print("Roll no:=",value[0])
    print("Reg no:=",value[1])
    print("mobile no:=",value[2])
    print("address :=",value[3])


n= input("enter your name ")
r= input("enter your Roll no ")
re= input("enter your reg no ")
m= input("enter your mobile no ")
a= input("enter your Address ")

Biodata(n,r,re,m,a)