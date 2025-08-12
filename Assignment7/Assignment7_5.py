def main():
    string = input("Enter a string: ")
    reversed_string = string[::-1]
    if reversed_string == string:
        print("The string is palindrome ")
    else:
        print("the string is not palindrome ")

    # string = input("string :")
    # reverse = string[0::-1]
    # print(reverse)

if __name__ == "__main__":
    main()