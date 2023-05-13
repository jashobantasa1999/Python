# WAP to perform following computation on stack using function like push, 
# pop, isempty, isfull, peak and use class and objects and multilevel inheritence
# I. Create an stack of user defined size using list
# II. Insert 20 user defined values in the stack using is full and push 
# operation in stack
# III. Search for an user defined element in the stack using peak 
# operation of stack
# IV. Delete 5 elements from stack using pop opeartion
# V. Display all remaig elements of stack
   
class Stack:
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
   
class Stack1(Stack):
    def popelment(self,a):
       
        for i in  range(5):
           if(self.isempty!=True):
              a.remove(a[self.top-1])
              self.top -=1
       
        return a
        
        
    def isempty(self):
        if(self.top==self.bottom):
            return True;
        else:
            return False
        
class Stack2(Stack1):
    def peak(self,a,b):
        if(b in a):
            print("index is ",a.index(b))
        else:
            print(b,"is not in the list")


b = int (input("enter the size of stack"))

a =[]
q = Stack2()
a = q.push(a,b)
print ("the list is ",a)

d = int (input("enter the no you want to search"))
q.peak(a,d)

a = q.popelment(a)

print (a)