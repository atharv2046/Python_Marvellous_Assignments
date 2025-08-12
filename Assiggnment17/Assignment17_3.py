import schedule
import time
import datetime

def coding():
    print("Do Coding -",datetime.datetime.now())

def main():
    schedule.every(30).minutes.do(coding)

    while True :
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()
 