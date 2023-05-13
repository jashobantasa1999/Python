# 2. WAP to perform following computation on queue using function like insert,
# delete, isempty, isfull, peak and use class and object with multiple inheitence
# VI. Create an queue of user defined size using list
# VII. Insert 20 user defined values in the queue using is full and insert
# operation in stack
# VIII. Search for an user defined element in the queue using peak
# operation of stack
# IX. Delete 5 elements from queue using delete opeartion
# X. Display all remaig elements of queue

class Queue:
    top =0
    bottom = 0
    
    def isnotfull(self,a,b):
        if(self.top==b):
            return False;
        elif(self.top<b):
            return True
    def push(self,a,b):
         for i in range(b):
             if(self.isnotfull(a,b)):
                c = int (input("Enter a no"))
                a.append(c)
                self.top +=1
        

         return a
   
class Queue1(Queue):
    def popelment(self,a):
       
        for i in  range(5):
           if(self.isempty!=True):
              a.remove(a[self.bottom])
              self.top -=1
        
        return a
        
        
    def isempty(self):
        if(self.top==self.bottom):
            return True;
        else:
            return False
        
class Queue2(Queue1):
    def peak(self,a,b):
        if(b in a):
            print("index is ",a.index(b))
        else:
            print(b,"is not in the list")


b = int (input("enter the size of Queue"))

a =[]
q = Queue2()
a = q.push(a,b)
print ("the list is ",a)

d = int (input("enter the no you want to search"))
q.peak(a,d)

a = q.popelment(a)

print (a)