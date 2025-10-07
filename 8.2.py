import time
import threading

account_balance = 1000

def perform_transaction(amount, customer, transaction_type, to_customer=None):
    """
    Performs a transaction on the account balance.

    Args:
        amount (int): The amount to deposit or withdraw.
        customer (str): The name of the customer initiating the transaction.
        transaction_type (str): The type of transaction ("deposit", "withdraw", or "transfer").
        to_customer (str, optional): The recipient of the transfer, if applicable. Defaults to None.
    """
    global account_balance
    
    if transaction_type == "deposit":
        print(f"[{customer}] Initiating deposit of ${amount}...")
        time.sleep(2)
        account_balance += amount
        print(f"[{customer}] Deposit successful! New Balance: ${account_balance}")
    elif transaction_type == "withdraw":
        print(f"[{customer}] Requesting withdrawl of ${amount}")
        time.sleep(2)
        if account_balance >= amount:
            account_balance -= amount
            print(f"[{customer}] Withdrawl Successful! New Balance: ${account_balance}")
        else:
            print(f"[{customer}] Insufficient funds! Current balance: ${account_balance}")
    elif transaction_type == "transfer":
        print(f"[{customer}] initiating transfer of ${amount} to {to_customer}...")
        time.sleep(2)
        if account_balance >= amount:
            account_balance -= amount
            print(f"[{customer}] Transfer successful! New balance: ${account_balance}")
            print(f"[{to_customer}] Recieved ${amount} from {customer}")
        else:
            print(f"[{customer}] Transfer failed! Insufficient funds.")

def deposit(amount, customer):
    """Deposits money into the account."""
    perform_transaction(amount, customer, "deposit")

def withdraw(amount, customer):
    """Withdraws money from the account."""
    perform_transaction(amount, customer, "withdraw")

def checkbalance(customer):
    """Checks the account balance."""
    print(f"[{customer}] Checking balance... Current balance: ${account_balance}")

def transfer(amount, from_customer, to_customer):
    """Transfers money from one customer to another."""
    perform_transaction(amount, from_customer, "transfer", to_customer)

transactions = [
    threading.Thread(target=deposit, args=(500, "Ajay")),
    threading.Thread(target=withdraw, args=(200, "Kunal")),
    threading.Thread(target=checkbalance, args=("John",)),
    threading.Thread(target=transfer, args=(300, "Venus", "Ruhi")),
    threading.Thread(target=withdraw, args=(800, "Kevin"))
]

print("***Initial Account Balance: ", account_balance, "***")
for t in transactions:
    t.start()

for t in transactions:
    t.join()

print("All banking transactions completed!...")