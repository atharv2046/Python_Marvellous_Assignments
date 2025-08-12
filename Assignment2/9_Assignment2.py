def count_digits(num):
    if num == 0:
        count = 1
    else:
        count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

def main():
    num = int(input("Enter a number :"))

    result = count_digits(num) 

    print("number of digits are :",result)

if __name__ == "__main__":
    main()

