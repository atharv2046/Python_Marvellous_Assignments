def print_stars(n):
    for i in range(n):
        for j in range(n):
            print('*', end='')
        print() 

def print_space(n):
    for i in range(n):
        print(' ', end='')
    print()

    
def main():
    number = int(input("Enter a number: "))
    print("Square of stars:")
    print_stars(number)

if __name__ == "__main__":
    main()
