class BankAccount():
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account holder Name:", self.Name, "Amount:", self.Amount)


    def Deposit(self):
        deposit = float(input("Enter the amount to deposit:"))
        self.Amount += deposit
        print("updadated amount is :",self.Amount)
    
    def Withdraw(self):
        withdraw = float(input("Enter the amount to withdraw :"))
        if withdraw <= self.Amount:
            self.Amount -= withdraw
            print("Withdrawal successful. Remaining amount:", self.Amount)
        else:
            print("Insufficient balance.")

    def CalculateInterest(self):
        interest = self.Amount * BankAccount.ROI / 100
        print("Interest on current balance is:", interest)


acc = BankAccount("Atharv", 1000)
acc.Display()
acc.Deposit()
acc.Withdraw()
acc.CalculateInterest()
