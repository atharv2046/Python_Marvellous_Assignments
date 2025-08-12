from multiprocessing import Pool

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def main():
    # print("Enter a number of your choice :")
    # num = int(input())

    # factorial(num)
    numbers = [3, 4, 6, 5, 8, 7]
    
    with Pool() as pool: 
        result = pool.map(factorial, numbers)
    
    print("Factorials:", result)

if __name__ == "__main__":
    main()







