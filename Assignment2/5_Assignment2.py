def ChkPrime(num):
    if num <= 1:
        print("1 is not prime number")
        return
    for i in range (2,num):
        if (num %i ==0):
            return False
    return True
    



def main():
    Number = int(input("Enter a number :"))

    prime = ChkPrime(Number)
    if prime :
        print("Number is prime :")
    else:
        print("number is not prime")


if __name__ == "__main__":
    main()