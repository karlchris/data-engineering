"""
    Handling Bank Account

    Task 1
        In the Account class, implement the getBalance() method that returns balance.

    Task 2
        In the Account class, implement the deposit(amount) method that adds amount to the balance. It does not return anything.

        Input
            balance = 2000
            deposit(500)
            getbalance()
        
        Output: 2500

    Task 3
        In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance. It does not return anything.
    
        Input
            balance = 2000
            withdrawal(500)
            getbalance()

        Output: 1500
    
    Task 4
        In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current balance. Below is the formula for calculating the interest amount:
        interest_amount = (interest_rate * balance) / 100

        Input
            balance = 2000
            interestRate = 5
            interestAmount()

        Output: 100
"""

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        # write code here
        pass

    def deposit(self, amount):
        # write code here
        pass

    def getBalance(self):
        # write code here
        pass


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        # write code here
        pass


# code to test - do not edit this
demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object
