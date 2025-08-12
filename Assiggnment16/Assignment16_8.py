def main():
    source = input("Enter the source file name :")
    destination = input("Enter the destination file name :")

    fobj1 = open(source, 'r')
    fobj2 = open(destination , 'w')
    for line in fobj1:
        if line.strip():
            fobj2.write(line)
    print("blank line are removed and output saved to the destination file")
if __name__ == "__main__":
    main()