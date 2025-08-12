
from marvellousnum import Chkprime

def sum(Numbers):
    sum_primes = 0
    for num in Numbers:
        if Chkprime(num):
            sum_primes += num
    return sum_primes


def listprime():
    Numbers = []
    n = int(input("How many numbers do you want to enter? "))

    for i in range(n):
        num = int(input())
        Numbers.append(num)
    print(Numbers)
        
    ret = sum(Numbers)
    print("Addition of all prime numbers is:", ret)

if __name__ == "__main__":
    listprime()
