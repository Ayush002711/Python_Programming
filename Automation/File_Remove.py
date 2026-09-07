import os

def main():
    try:
        os.remove("Demo.txt")

        fobj.remove()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")
if __name__=="__main__":
    main()

