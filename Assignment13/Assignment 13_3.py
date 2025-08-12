class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        sum_factors = sum([i for i in range(1, self.Value) if self.Value % i == 0])
        return sum_factors == self.Value

    def Factors(self):
        print("Factors of", self.Value, "are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = sum([i for i in range(1, self.Value + 1) if self.Value % i == 0])
        return total

num1 = Numbers(28)
print("Is Prime:", num1.ChkPrime())
print("Is Perfect:", num1.ChkPerfect())
num1.Factors()
print("Sum of Factors:", num1.SumFactors())
