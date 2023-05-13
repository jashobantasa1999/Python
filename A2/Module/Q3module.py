# 3. WAP to perform following computation on queue using function like insert,
# delete, isempty, isfull, peak and use function and module
# VI. Create an queue of user defined size using list
# VII. Insert 20 user defined values in the queue using is full and insert
# operation in stack
# VIII. Search for an user defined element in the queue using peak
# operation of stack
# IX. Delete 5 elements from queue using delete opeartion
# X. Display all remaig elements of queue

def push(a,b):
    a.append(b)
   
def popelment(a):
    a.removed(a[0])
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
