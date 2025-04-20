class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


    def show_balance(self):
        return self.balance


    def display(self):
        print("Account Number:", self.acc_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


accounts = []


def find_account(acc_no):
    for acc in accounts:
        if acc.acc_no == acc_no:
            return acc
    return None


while True:
    print("\nBanking Operations Menu")
    print("1. New Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Show All Accounts")
    print("6. Exit")


    choice = input("Enter your choice: ")


    if choice == '1':
        acc_no = input("Enter account number: ")
        name = input("Enter account holder name: ")
        bal = float(input("Enter initial deposit: "))
        acc = BankAccount(acc_no, name, bal)
        accounts.append(acc)
        print("Account created successfully.")


    elif choice == '2':
        acc_no = input("Enter account number: ")
        acc = find_account(acc_no)
        if acc:
            amount = float(input("Enter amount to deposit: "))
            acc.deposit(amount)
            print("Amount deposited.")
        else:
            print("Account not found.")


    elif choice == '3':
        acc_no = input("Enter account number: ")
        acc = find_account(acc_no)
        if acc:
            amount = float(input("Enter amount to withdraw: "))
            if acc.withdraw(amount):
                print("Amount withdrawn.")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")


    elif choice == '4':
        acc_no = input("Enter account number: ")
        acc = find_account(acc_no)
        if acc:
            print("Balance:", acc.show_balance())
        else:
            print("Account not found.")


    elif choice == '5':
        if len(accounts) == 0:
            print("No accounts available.")
        else:
            for acc in accounts:
                acc.display()
                print("------------")


    elif choice == '6':
        print("Exiting banking system...")
        break


    else:
        print("Invalid choice.")
