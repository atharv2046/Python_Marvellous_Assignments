def print_stars(number):
    for i in range(number):
        print("*",end="")

def main ():
    number = int(input("Enter a Number"))

    print_stars(number)

    

if __name__ == "__main__":
    main()