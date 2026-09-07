def main():
    try:
        fobj=open("Demo.txt","r")

        print("File gets Opened")

        fobj.seek(10,0)

        Data=fobj.read

        print(Data)

    except FileNotFoundError as fobj:
        
        print("File is not present in current directory")
if __name__=="__main__":
    main()
