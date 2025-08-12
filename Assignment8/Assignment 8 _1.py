import threading

def printeven():
    print("Even Thread")
    for i in range(0,20,2):
        print(i)
    print("Even thread finished")

def printodd():
    print("Odd Thread")
    for i in range (1, 20,2):
        print(i)
    print("Odd thread is finished")


even_thread = threading.Thread(target=printeven,name= 'even')
odd_thread = threading.Thread(target = printodd,name = 'odd')

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()