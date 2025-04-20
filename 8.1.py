
import threading
import time


def atm_transaction(user,transaction):
    print(f"{user} is performing {transaction}...")
    time.sleep(2)
    print(f"{user} completed {transaction}.")
    
thread1 = threading.Thread(target=atm_transaction,args=("Amar","Cash Withdrawl"))
thread2 = threading.Thread(target=atm_transaction,args=("Ajay","Balance Inquiry"))
thread3 = threading.Thread(target=atm_transaction,args=("Ashish","Money Deposit"))


thread1.start()
thread2.start()
thread3.start()


thread1.join()
thread2.join()
thread3.join()


print("All transactions completed.")
