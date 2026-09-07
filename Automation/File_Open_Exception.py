def main():
    try:
        open("Demo.txt","r")
        print("File gets open")

    except FileNotFoundError as fobj:
        print("File is not present in current directory")
if __name__=="__main__":
    main()

    