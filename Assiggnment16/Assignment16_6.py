def main():
    try :
        source = input("Enter the source filename :")

        destination = input("Enter the destination file name :")

        src = open(source , 'r')
        dest = open(destination , 'w')
        for line in src :
            dest.write(line)
            
        print("file copied Sucessfully ")

    except FileNotFoundError :
        print("The file {source} does not existt")

if __name__ == "__main__":
    main()