# 4. WAP to perform following using module and function for
# deposit,withdraw,check balance for banking application
# I. Assign a fixed value as balance for account
# II. Deposit user defined amount and display updated balance
# III. Withdraw user defined money if user has sufficient fund otherwise
# shoe insufficient fund
# IV. Check for balance
# V. Maintain a fixed amount 3000 in the accpunt


balance = 3000  

def deposit(amount):
    global balance 
    balance += amount
    print(f"Deposit successful! Updated balance: {balance}")

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
        print(f"Withdrawal successful! Updated balance: {balance}")
    else:
        print("Insufficient funds.")

def check_balance():
    global balance
    print(f"Current balance: {balance}")
