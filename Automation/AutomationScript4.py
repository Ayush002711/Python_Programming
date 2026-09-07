import sys

def main():
    if(len(sys.argv) ==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script is used to travel the Directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the script as")
            print("Python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            DirectoryName=sys.argv[1]
            print("Directory name is:",DirectoryName)
    else:
        print("Invalid Number of arguements")
        print("Please use --h or  --u for more information")
   
if __name__=="__main__":
    main()

    