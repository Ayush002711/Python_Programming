import sys
import os
import time
import schedule

def DirectoryScanner(DirectoryPath):
    Border="-"*40

    timestamp=time.ctime()

    LogFilename="Marvellous%s.log"%(timestamp)  
    LogFilename= LogFilename.replace("","_")
    LogFilename=LogFilename.replace(" ","_")

    Ret=False

    Ret=os.path.exists(DirectoryPath)

    if(Ret==False):
        print("Marvellous Automation Error: There is no such Directory with name",DirectoryPath)
        return
    
    Ret=os.path.isdir(DirectoryPath)

    if(Ret==False):
        print("Marvellous Automation Error:It is not a Directory with name",DirectoryPath)
        return

    print("Log File gets created with name:",LogFilename)  

    fobj=open(LogFilename,"w")

    fobj.write(Border+"\n")
               
    fobj.write("Marvellous Automation Script\n")
    fobj.write(Border+"\n\n")

    fobj.write("Files from the Directory :\n\n")
    fobj.write(Border+"\n")

    TotalFiles=0
    EmptyFiles=0


    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            fobj.write(f"{fname} :{+os.path.getsize(fname)}bytes\n")

            if(os.path.getsize(fname)==0):
                EmptyFile=EmptyFile+1
                os.remove(fname)
    fobj.write(Border+"\n")
    fobj.write(f"Total Files scanned :{TotalFiles}\n")
    fobj.write(f"Total empty files found and deleted:{EmptyFiles}\n")

    fobj.write(Border+"\n")
    fobj.write("Log files get Created at :"+timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()

def main():
    Border="-"*40
    print(Border)
    print("Marvellous Automation Script")
    print(Border)
  
    if(len(sys.argv) ==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script is used to travel the Directory")
            print("For better usage please check --u flag")
            
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the script as")
            print("Python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            
            while True:
                schedule.run_pending()
                time.sleep(1)
                           
    else:
        print("Invalid Number of arguements")
        print("Please use --h or  --u for more information")

    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)
   
if __name__=="__main__":
    main()




    
    