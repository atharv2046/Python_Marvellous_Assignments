def main():
    filename = input("ENter file name :")

    try:
        with open(filename,'r')as file:
            content = file.read()
            print("File Contents :\n",content)
    except FileNotFoundError:
        print(filename+"not found.")

if __name__ == "__main__":
    main()