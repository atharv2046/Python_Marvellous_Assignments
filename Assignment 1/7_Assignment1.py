def divisibleby5(num):
    if (num % 5 == 0):
        return True

    else: return False

def main():

    num  = int(input("Enter a number: "))

    result = divisibleby5(num)

    print(result)


if __name__ == "__main__":
    main()
    

