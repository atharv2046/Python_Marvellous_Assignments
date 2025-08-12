def Print_stars(n):
    for i in range(n,0 ,-1):
        print("*" * i)


def main():

    number = int(input("Enter a number:"))

    stars = Print_stars(number)

    print("The output is :",stars)



if __name__ == "__main__":
    main()