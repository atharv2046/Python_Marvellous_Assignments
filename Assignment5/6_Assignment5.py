def CtoF(celsius):
    Fahrenheit = (celsius * 9/5)+32
    return Fahrenheit

def main():
    print("enter a temperature in celsius:")
    temp =float(input())

    far = CtoF(temp)
    print("Temperature in Fahrenheit",far)

if __name__ == "__main__":
    main()