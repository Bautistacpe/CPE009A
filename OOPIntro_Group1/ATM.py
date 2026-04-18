"""
    ATM.py
"""

class ATM():
    def __init__(self, serial_number, account_number, current_balance):
        self.serial_number = serial_number
        self.account_number = account_number
        self.current_balance = current_balance
        
    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        print("Deposit Complete!")
        
    def withdraw(self, account, amount):
        account.current_balance = account.current_balance - amount
        print("Withdraw Complete!")
        
    def check_currentbalance(self, account):
        print(account.current_balance)        
        
    def view_transactionsummary(self, account, amount):
        print("Transaction Summary for Account", account.account_number)
        print("Deposited", amount, "in Account", account.account_number)
        print("Checked Balance for Account", account.account_number, ". Current Balance:", account.current_balance)
        print()