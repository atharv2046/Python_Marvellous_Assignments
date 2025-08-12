import os 
def main():
    filename = "sample.txt"

    if os.path.exists(filename):
        
        fobj = open(filename, "r")
        lines = fobj.readlines()
        line_count = len(lines)

        wordscount = 0
        charcount = 0

        for line in lines:
            words = line.split()
            wordscount = wordscount + len(words)
            charcount  += len(line)


        print("Lines :",line_count)
        print("Words :",wordscount)
        print("Characters :",charcount)
    else:
        print("file not found")

if __name__ == "__main__":
    main()