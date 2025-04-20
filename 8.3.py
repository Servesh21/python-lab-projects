
import time
import threading
lock = threading.Lock()
account_balance=1000


def deposit(amount,customer):
    global account_balance
    with lock:
        print(f"[{customer}] Initiating deposit of ${amount}...")
        time.sleep(2)
        account_balance += amount
        print(f"[{customer}] Deposit successful! New Balance: ${account_balance}")
    
def withdraw(amount,customer):
    global account_balance
    with lock:
        print(f"[{customer}] Requesting withdrawl of ${amount}")
        time.sleep(2)
        if account_balance >= amount :
            account_balance -= amount
            print(f"[{customer}] Withdrawl Successful! New Balance: ${account_balance}")
        else:
            print(f"[{customer}] Insufficient funds! Current balance: ${account_balance}")
        
def checkbalance(customer):
    with lock:
        print(f"[{customer}] Checking balance... Current balance: ${account_balance}")
    
def transfer(amount,from_customer,to_customer):
    global account_balance
    with lock:
        print(f"[{from_customer}] initiating transfer of ${amount} to {to_customer}...")
        time.sleep(2)
        if account_balance >= amount:
            account_balance -= amount
            print(f"[{from_customer}] Transfer successful! New balance: ${account_balance}")
            print(f"[{to_customer}] Recieved ${amount} from {from_customer}")
        else:
            print(f"[{from_customer}] Transfer failed! Insufficient funds.")
        
transactions = [
    threading.Thread(target=deposit,args=(500,"Ajay")),
    threading.Thread(target=withdraw,args=(200,"Kunal")),
    threading.Thread(target=checkbalance,args=("John",)),
    threading.Thread(target=transfer,args=(300,"Venus","Ruhi")),
    threading.Thread(target=withdraw,args=(800,"Kevin"))
]


print("***Initial Account Balance: ",account_balance,"***")
for t in transactions:
    t.start()
    
for t in transactions:
    t.join()
    
print("All banking transactions completed!...")
