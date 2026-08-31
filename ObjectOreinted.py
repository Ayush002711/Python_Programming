class Arithematic:
    def Addition(No1,No2):
        Ans=No1+No2
        return Ans
    def Substraction(No1,No2):
        Ans=No1-No2
        return Ans
    
Aobj=Arithematic()

print("Enter First Number")
Value1=int(input())

print("Enter Second Number")
Value2=int(input())

Ret=Aobj.Addition(Value1,Value2)    #Error
print("Addition is :",Ret)

Ret=Aobj.Substraction(Value1,Value2)  #Error
print("Substraction is :",Ret)






