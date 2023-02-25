# c) categories the password as low medium and high
#  low – only numbers or alphabets and length less than 8
#  medium- number and alphabets and length more than 8
#  string- number, alphabet and special character should present 
# and length should be greater than 

a = input("enter your password")

if(a.isnumeric() or a.isalpha() and len(a)<8):
    print("low")
elif(len(a)>8):
    if(a.isalnum()):
        print("Medium")
    elif(a.isascii() ):
        print("Strong")
else:
    print("invalid Password")


