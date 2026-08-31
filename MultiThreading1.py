import threading

def Display():
    print("Inside Display:",threading.get_ident())

def main():
    Display()
    print("Inside Display:",threading.get_ident())
    
if __name__=="__main__":
    main()
