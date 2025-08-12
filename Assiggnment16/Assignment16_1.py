def main():
    filename = input("enter a name of file that you want to create :")

    fobj = open(filename,"w")

    data = input("Enter the data that you want to add into file :")

    fobj.write(data)
    fobj.close

if __name__ == "__main__":
    main()
