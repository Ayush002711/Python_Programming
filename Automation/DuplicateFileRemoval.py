import os
import sys
import schedule
import time
import hashlib
import smtplib
from email.message import EmailMessage

def CalculateChKsum(Filename):
    fobj = open(Filename,"rb")

    hobj=hashlib.md5()

    Buffer=fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DeleteDuplicate(DirectoryPath):
    Ret=False

    Ret = os.path.exists(DirectoryPath)

    Duplicate=dict()

    if(Ret==False):
        print("Marvellous Automation Error: There is no such Directory with name",DirectoryPath)
        return
            
    Ret=os.path.isdir(DirectoryPath)
        
    if(Ret==False):
        print("Marvellous Automation Error:It is not a Directory with name",DirectoryPath)
        return

    Timestamp=time.strftime("%d-%m-%Y_%H-%M-%S")
    FileName=os.path.join(DirectoryPath,f"FileLog_{Timestamp}.log")

    for FolderName,SubFolder,Files in os.walk(DirectoryPath):
        for fname in Files:
            fname=os.path.join(FolderName,fname)

            checksum=CalculateChKsum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)

            else:
                Duplicate[checksum]=[fname]

    log=open(FileName,"a")
    log.write("-"*100+"\n")
    log.write("DUPLICATE FILES REMOVAL LOG "+"\n")
    log.write("-"*100+"\n")
    log.write(f"\n Log File Created at  :{time.ctime()}")
    log.write("\n\n\n")
    log.write("-"*100+"\n")
    log.write("DUPLICATE FILES :-\n")

    for checksum in Duplicate:
        if len(Duplicate[checksum])>1:
            log.write("-"*100+"\n")
            log.write(f"Checksum Value :{checksum}\n")
            value=Duplicate.get(checksum)
            log.write(f"File name Associatedd with :{value}\n")
            log.write("-"*100+"\n")

    Total_files=0
    for Files in Duplicate.values():
        Total_files +=len(Files)

    log.write("-"*100+"\n")
    log.write("Deleted Files:\n")
    log.write("-"*100+"\n")

    Total_Duplicate=0

    for FileList in Duplicate.values():
        if len(FileList)>1:
            Total_Duplicate+=len(FileList)-1

    Total_DuplicatefilesDeleted=0
    for checksum in Duplicate:
        if len(Duplicate[checksum])>1:
            for DuplicateFile in Duplicate[checksum][1:]:
                Total_DuplicatefilesDeleted+=1
                log.write(f"Checksum:{checksum}\n")
                log.write(f"Deleted file:{DuplicateFile}\n")
                os.remove(DuplicateFile)

                log.write("-"*100+"\n")

    log.write("Log File Ends\n")

    log.write("-"*100+"\n")
    log.close()

    fobj=open("MailBody.txt","w")
    fobj.write("Jay Ganesh\n")

    fobj.write("The Duplicate Removal has been completed succesfully")
    fobj.write(f"Starting Time:{time.ctime()}\n")
    fobj.write(f"\n\n Total Files Scanned:{Total_files}\n")
    fobj.write(f"Total Duplicate files:{Total_Duplicate}\n")
    fobj.write(f"Total Duplicate files Deleted:{Total_DuplicatefilesDeleted}\n")
    fobj.write(f"Time of Deletion:{time.ctime()}\n")
    fobj.close()

    MailFileReciever(FileName,sys.argv[2])

def MailFileReciever(Filename,reciever):
    mail=EmailMessage()
    mail["From"]="File Survillence System."
    mail["To"]=reciever
    mail["Subject"]=(F"File Deletion of Log File:{time.ctime()}")
    objbody=open("MailBody.txt","r")
    body=objbody.read()

    mail.set_content(body)

    attachment=open(Filename,"rb")
    data=attachment.read()
    name=attachment.name
    attachment.close()

    mail.add_attachment(data,maintype="text",subtype="plain",filename=name)
    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)
    smtp.login("ayushjadhav0027@gmail.com","Ayush@0027")
    smtp.send_message(mail)
    print("Mail sent succesfully")
    smtp.quit()

def main():
    Border="-"*50
    print(Border)
    print("Duplicate File Removal Automation Started")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("It identifies duplicate files")
            print("Also deletes duplicate file")
            print("It generates detailed log file")
            print("It send the log file through email")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the script as")
            print("Python FileName.py DirectoryPath EmailID")

    elif len(sys.argv)==3:
        schedule.every(1).minutes.do(DeleteDuplicate,sys.argv[1])

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