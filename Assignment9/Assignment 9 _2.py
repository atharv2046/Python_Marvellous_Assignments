
from multiprocessing import Process

def square_number(n):
       print("the square list is :",n*n)
    

if __name__ == "__main__":

    user_input = input("Enter numbers separated by space: ")
    numbers = []
    for s in user_input:
        num = int(s)
        numbers.append(num)
        processes = []

    for num in numbers:
        p = Process(target=square_number, args=(num,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
 