import threading

def evenfactor(num):
    sum_even = 0
    for i in range(1,num+1):
        if num % i == 0 and i%2 == 0:
            sum_even += i
    print("sum of even factors",sum_even) 

def oddfactor(num):
    sum_odd = 0
    for i in range (1,num+1):
       if num % i == 0 and i % 2 != 0:
        sum_odd += i
    print("sum of odd factors",sum_odd) 

def main():
    num = int(input("Enter a number: "))

    t1 = threading.Thread(target=evenfactor, args=(num,))
    t2 = threading.Thread(target=oddfactor, args=(num,))

    t1.start()
    t2.start()

    t1.join()  
    t2.join()

    print("exit from main")

if __name__ == "__main__":
    main()   
