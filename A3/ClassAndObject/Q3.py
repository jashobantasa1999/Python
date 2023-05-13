# Wap to display the order in which constructors and destructors are
# invoked during runtime in class ?
class MyClass:
    def __init__(self):
        print("Default constructor invoked")

    def __init__(self, value):
        self.value = value
        print("Parameterized constructor invoked with value", value)
        
    def __del__(self):
        print("Destructor invoked")


obj1 = MyClass()
obj2=MyClass(12)





