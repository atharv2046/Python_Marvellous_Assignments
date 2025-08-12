def main():
    try :
        filename = input("Enter the filename you want to read")

        fobj = open(filename , "r")
        for line in fobj:
            words = line .strip().split()
            if len(words)>5:
                print(line.strip())
        fobj.close()
    except FileNotFoundError :
        print("The file {filename} does not exist")


if __name__ == "__main__":
    main()