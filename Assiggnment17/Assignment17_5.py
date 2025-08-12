import schedule
import time 
import datetime 

def myschedule():
    current_time = str(datetime.datetime.now())
    print("Current Time -", current_time)

    filename = "Marvellous.txt"
    with open(filename, 'a') as fobj:
        fobj.write("Current Time - " + current_time + "\n")

def main():
    schedule.every(5).minutes.do(myschedule)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main() 
