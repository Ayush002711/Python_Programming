def BigBazar():
    print("Inside BigBazar")
    
    def Amul():
            print("Inside Amul Icecream parlor")

def main():
     BigBazar()       #allowed
     BigBazar.Amul()  #error
     Amul()           #error
if __name__=="__main__":
    main()
    
