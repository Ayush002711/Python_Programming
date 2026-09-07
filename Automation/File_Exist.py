import os

def main():
    Ret = os.path.exists("Demo.txt")

    if(Ret==True):
        print("File is present in current directory")
    else:
        print("There is nu such File")
if __name__=="__main__":
    main()

    


