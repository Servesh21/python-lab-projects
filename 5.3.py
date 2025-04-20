class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited ${amount}.\nNew Balance: ${self.balance}")
        
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}.\nNew Balance: ${self.balance}")
            
            
class SavingsAccount(BankAccount):
    def __init__(self,account_holder,balance,rate):
        super().__init__(account_holder,balance)
        self.rate = rate
        
    def add_interest(self):
        interest = self.balance * self.rate / 100
        self.balance += interest
        print(f"Interest added : ${interest}.\n New Balance: ${self.balance}")
        
class CurrentAccount(BankAccount):
    def __init__(self,account_holder,balance,limit):
        super().__init__(account_holder,balance)
        self.limit = limit
        
    def withdraw(self,amount):
        if amount > self.balance + self.limit:
            print("Transaction declined. Overdraft limit exceeded,")
            
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}.\nRemaining balance: ${self.balance}")
            #super().withdraw(amount)
            
print("===Savings Account===")
savings = SavingsAccount("Ajay",5000,3)
print(f"Account Holder : {savings.account_holder}")
print(f"Initial Balance : ${savings.balance}")
savings.deposit(1000)
savings.withdraw(2000)
savings.add_interest()
print()
print("===Current Account===")
current = CurrentAccount("Rohan",2000,1000)
print(f"Account Holder : {current.account_holder}")
print(f"Initial Balance : ${current.balance}")
current.deposit(500)
current.withdraw(3000)
current.withdraw(1000)
