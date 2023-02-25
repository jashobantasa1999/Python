# 5. Write a Python program
# I. To add 'ing' at the end of a given string (length should be at least
# 3). If the given string already ends with 'ing' then add 'ly' instead. If
# the string length of the given string 5. is less than 3, leave it
# unchanged. Sample String : 'abc' Expected Result : 'abcing' Sample
# String : 'string' C 220.2 Expected Result : 'stringly'
# II. To get a string from a given string where all occurrences of its first
# char have been changed to '$', except the first char itself
a = input("enter a string")

if len(a) >=3:
    if(a.endswith("ing")):
        a = a+"ly"
    else:
        a= a+"ing"

print(a)
