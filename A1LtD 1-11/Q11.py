# 11. WAP to do following using string
#  a) Check whether a string is palindrome or not
a = input("enter a string  ")
b=a[::-1]

if a==b:
    print("it is palindrom")
else:
    print(" it is not a palindrome")
