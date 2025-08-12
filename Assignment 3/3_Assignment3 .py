def Addlist():
    Numbers = []
    list = int(input("how many numbers you want to add into a list ?"))

    for i in range(list):
        print("Enter a number :",i+1)
        num = float(input())
        Numbers.append(num)
    return Numbers

def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num <min_num:
            min_num = num
    return min_num


def main():

    newlist = Addlist()

    min_number = find_min(newlist)
    print("Your list is ",newlist)
    print("The Minimun number is ",min_number)

if __name__ == "__main__":
    main()



