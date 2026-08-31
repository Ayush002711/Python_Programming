import time

#2+4+6+8=20

def SumEven(No):
    Sum=0
    for i in range(2,No,2):
        Sum=Sum+i
    print("Summation of even is:",Sum)

#1+3+5+7+9=25

def SumOdd(No):
    Sum=0
    for i in range(1,No,2):
        Sum=Sum+i
    print("Summation of odd is:",Sum)

def main():

    start_time=time.perf_counter()

    SumEven(10000000)
    SumOdd(10000000)

    end_time=time.perf_counter()
    
    print(f"Time is required :{end_time - start_time:.4}")
if __name__=="__main__":
    main()
 
 