# Write a python program to store details of a student like rollno, regdno,
# name, branch, stream, sem, phone no,address in dictionary and print the
# details in cv format
dict ={}

name = input("enter your name")
dict["name"]= name

roll = int(input("enter your roll"))
dict["roll"]= roll
reg = int(input("enter your reg"))
dict["reg"]= reg
branch = input("enter your branch")
dict["branch"]= branch
sem= int(input("enter your sem"))
dict["sem"]= sem
phone= int(input("enter your phone"))
dict["phone"]= phone
address = input("enter your address")
dict["address"]= address

print(dict)