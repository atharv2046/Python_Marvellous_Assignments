def Addlist():
    Numbers = []
    list = int(input("how many numbers you want to add into a list ?"))

    for i in range(list):
        print("Enter a number :",i+1)
        num = float(input())
        Numbers.append(num)
    return Numbers

def find_Max(numbers):
    max_num = 0
    for num in numbers:
        if num >max_num:
            max_num = num
    return max_num


def main():

    newlist = Addlist()

    max_number = find_Max(newlist)
    print("Your list is ",newlist)
    print("The Maximum number is ",max_number)

if __name__ == "__main__":
    main()



