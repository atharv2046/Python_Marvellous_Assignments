import threading 

def small(text):
    count = 0
    for char in text:
        if char.islower():
            count += 1
    print(threading.get_ident())

def capital(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    print(threading.get_ident())

def digit(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    print(threading.get_ident())

# input_string = "ATHARVSONDGE123PROGRAMming456"




t1 = threading.Thread(target=small, args=("small",))
t2 = threading.Thread(target=capital, args=("Captial",))
t3 = threading.Thread(target=digit, args=("12345",))


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Main thread finished.")