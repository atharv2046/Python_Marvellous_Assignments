def main():
    even = 0
    for i in range(1,101):
        if i % 2 == 0:
            even  += i


    print("sum of even numbers from 1 to 100 :",even) 
    
if __name__ == "__main__":
    main()