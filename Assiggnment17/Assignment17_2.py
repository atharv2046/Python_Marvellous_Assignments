import schedule 
import time 
import datetime 


def Myschedule():
    print("Current time is ",datetime.datetime.now())

def main():
    
    schedule.every(20).seconds.do(Myschedule)
    
    while True : 
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()