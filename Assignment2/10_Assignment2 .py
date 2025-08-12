def Sumdigits(num):
    sum = 0
    while num>0:
        digit = num %10
        sum += digit
        num = num//10
    return sum 

def main():
    num = int(input("Enter a number"))

    result = Sumdigits(num)

    print("Sum of digits is :",result)


if __name__ == "__main__":
    main()