class Demo:
    Value1=10     #ClassVariable
    Value2=20


def __init__(self):
    self.No1 = 11
    self.No2 = 21

#Instance Method

def fun(self):
    print("Inside instance metho named as fun")
    print(self.No1)
    print(self.No2)
    print("Value1")
    print("Value2")

Aobj = Demo()
Aobj.fun()

