class Demo:
    Value1=10   
    Value2=21

def __init__(self):
    self.No1 = 11
    self.No2 = 20

obj1 = Demo()
obj2 = Demo()

obj1.No1=0


print(obj1.No1)
print(obj2.No2)

Demo.Value1= 0

print(Demo.Value1)
