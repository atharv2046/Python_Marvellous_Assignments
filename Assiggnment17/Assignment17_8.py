import schedule 
import time 
import datetime

def mailchecking():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # %Y" : year(4digits)y(2digits -year)(%M&%m -Month(00-59)&(01-12)) (%H -hour(00-23))

    print("Checking Mail...")


def main():
    schedule.every(10).seconds.do(mailchecking)
    print("Email Checker Started.Press ctrl+c to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()