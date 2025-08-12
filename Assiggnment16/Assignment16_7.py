def main():
    filename = "Marks.txt"

    fobj = open(filename , 'r')
    for line in fobj :
        parts = line.strip().split()
        if len(parts) >= 2:
            name = " ".join(parts[:-1])
            try:
                marks = int(parts[-1])
                if marks > 75:
                    print(f"{name} scored {marks}")
      
            except :
                print("Invalid marks for the student :",{line.strip()})


if __name__ == "__main__":
    main()