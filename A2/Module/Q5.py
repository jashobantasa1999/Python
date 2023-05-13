import Q5module as q

a =  int(input("enter a no for factorial"))

print("factorial of ",a,"is",q.factorial(a))

a= int (input("enter a no for gcd"))
b= int (input("enter a no for gcd"))


print(q.Gcd(a,b))
a= int (input("enter a no for lcm"))
b= int (input("enter a no for lcm"))


print(q.Lcm(a,b))
a= int (input("enter a 1st no for swap"))
b= int (input("enter a 2nd no for swap"))


a,b=q.swap(a,b)

print("1st no is ",a)
print("2nd no is ",b)

