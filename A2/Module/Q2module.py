# 2. WAP to perform following computation on stack using function like push,
# pop, isempty, isfull, peak and use function and module
# I. Create an stack of user defined size using list

def push(a,b):
    a.append(b)
   
def popelment(a):
    a.pop()
    return a
def isempty(a):
    if(len(a)==0):
        print("it is empty")
    else:
        print("it is not empty")
def isfull(a,b):
    if(len(a)==b):
        return True;
    elif(len(a)>b):
        return False
def peak(a,b):
    if(b in a):
        print("index is ",a.index(b))
    else:
        print(b,"is not in the list")
