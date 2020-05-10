# Abstruct Class
class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withDrawn(self, amount):

        if self.balance - amount >= self.min_balance:
            self.balance = self.balance - amount
        else:
            print("Balance is Low")
    
    def statement(self):
        print(f'{self.name}\' Account Balance: {self.balance}')
        return 0


# Inheritance
class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)
    
    def __str__(self):
        return f'{self.name}\' Savings Account Balance: {self.balance}'


class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)
    
    def __str__(self):
        return f'{self.name}\' Current Account Balance: {self.balance}'


s1 = Savings("Shovon", 2000)

print(s1.statement())