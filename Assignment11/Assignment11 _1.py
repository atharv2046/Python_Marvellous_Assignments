def numbers(n):
    if n==0:
        return
    numbers(n-1)
    print(n)

def main():
    numbers(5)

if __name__ == "__main__":
    main()