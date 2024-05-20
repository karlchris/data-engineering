""" Solution 1: Handling Bank Account """

class Account:  # parent class
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    # withdrawal method subtracts the amount from the balance
    def withdrawal(self, amount):
        self.balance = self.balance - amount
    
    # deposit method adds the amount to the balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    # this method just returns the value of balance
    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    # computes interest amount using the interest rate
    def interestAmount(self):
        return (self.balance * self.interestRate / 100)


obj1 = SavingsAccount("Steve", 5000, 10)
print("Initial Balance:", obj1.getBalance())
obj1.withdrawal(1000)
print("Balance after withdrawal:", obj1.getBalance())
obj1.deposit(500)
print("Balance after deposit:", obj1.getBalance())
print("Interest on current balance:", obj1.interestAmount())
