import threading

def evenlist(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    print("Sum of even numbers:", total)

def oddlist(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    print("Sum of odd numbers:", total)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


t1 = threading.Thread(target=evenlist, args=(nums,))
t2 = threading.Thread(target=oddlist, args=(nums,))


t1.start()
t2.start()

t1.join()
t2.join()

print("Main program done.")
