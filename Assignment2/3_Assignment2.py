def fact(n):
    fact = 1
    for i in range (1,n+1):
        fact = fact*i

    return fact



def main ():
    print("Enter a number:")
    number = int(input())

    factorial = fact(number)

    print("factorial is :",factorial)

if __name__ == "__main__":
    main()

