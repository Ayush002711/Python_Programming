import schedule
import time

def Display():
    print("Messii is GOAT...Messii is GOAT...Messii is GOAT..Messii is GOAT")
    
def main():
    schedule.every(5).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(2)
if __name__=="__main__":
    main()
