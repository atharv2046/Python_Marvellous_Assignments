def chkchr(chr):
    data = ["a","e","i","O","u","A","E","I","O","U"]
    for i in data:
        if(chr ==i):
            return True
    return False


def main():
    print("Enter a character:")
    char = (input())


    if chkchr(char):
        print("it is vowel")
    else:
        print("it is consonant")


if __name__ == "__main__":
    main()


