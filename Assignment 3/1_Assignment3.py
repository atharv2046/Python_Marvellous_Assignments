def Elements_list():
    numbers = []
    n = int(input("Enter a numbers you want to add inn list:"))

    for i in range(n):
        print("Enter number :",i+1,)
        num = float(input())
        numbers.append(num)
    return numbers
    
def Sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total 


def main():

    List = Elements_list()
    result = Sum(List)

    print("The sum of list is :",result)

if __name__ == "__main__":
    main()

