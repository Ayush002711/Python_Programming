import sys
import os
import hashlib

def CalculateCheckSum(FileName):
    fobj=open(FileName,"rb")

    hobj=hashlib.md5()

    Buffer=fobj.read(1000)

    while(len(Buffer)>0):
        hobj.update
        Buffer=fobj.read(1000)

    fobj.close()

    return hobj.hexdigest

def main():
    Ret=CalculateCheckSum("DemoX.txt")
    print("CheckSum of file is:",Ret)
if __name__=="__main__":
    main()
