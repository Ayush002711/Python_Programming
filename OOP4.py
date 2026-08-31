class Demo:
    Value1=10   
    Value2=21

def __init__(self):
    self.No1 = 11
    self.No2 = 21
def fun(self):
    print("Inside instance metho named as fun")
    print(self.No1)
    print(self.No2)
    print(Demo.Value1)
    print(Demo.Value2)

@classmethod
def gun(cls):
    
    print("Inside instance metho named as fun")
    #print(Demo.No1)  Not Allowed
    #print(Demo.No2)
    print(Demo.Value1)
    print(Demo.Value2)

dobj=Demo
dobj = gun()
