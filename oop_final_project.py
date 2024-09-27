import random


class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.account_number = random.randint(10000, 50000)
        self.name = name
        self.email = email
        self.address = address
        self.account_type =account_type
        self.balance = 0
        self.transaction_history = []
        self.loans = []
        self.loan_limit = 2


    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            self.transaction_history.append(amount)
            print(f"Deposit {amount}")
        else:
            print("Amount is not sufficient")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            self.transaction_history.append(amount)
            print(f"Withdraw {amount}")
        else:
            print("Withdrawal amount exceeded")

    def check_available_balance(self):
        print(f"Your current balance is: {self.balance}")

    def check_transaction_history(self):
        if not self.transaction_history:
            print("No transaction created yet.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(f"Transaction amount: {transaction}")

    def loan_taken(self, amount):
            if len(self.loans) < self.loan_limit:
                self.balance = self.balance + amount
                self.loans.append(amount)
                self.transaction_history.append(amount)
                print(f"loan {amount} granted")
            else:
                print("loan limit reached.")

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance = self.balance - amount
            other_account.balance = other_account.balance + amount
            other_account.transaction_history.append(amount)
            print(f"Transferred {amount}")
        else:
            print("Insufficient funds for the transfer.")


class Admin:
    def __init__(self) -> None:
       self.accounts = {} 
       self.total_balance = 0
       self.total_loan_amount = 0
       self.loan_feature = True


    def create_account(self, name, email, address, account_type):
        account = User(name, email, address, account_type)
        self.accounts[account.account_number] = account
        print(f"Account creat successfully. Account number: {account.account_number}")
        return account

    def delete_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts.pop(account_number)
            print(f"Account {account_number} deleted successfully.")
        else:
            print("Account not found")

    def user_account_list(self):
        return self.accounts
    
    def check_total_balance(self):
        self.total_balance = sum(account.balance for account in self.accounts.values())
        print(f"Total Bank Balance: {self.total_balance}")

    def check_total_loan_amount(self):
        self.total_loan_amount = sum(sum(account.loans) for account in self.accounts.values())
        print(f"Total loan amount: {self.total_loan_amount}")

    def loan_feature_available(self):
        if self.loan_feature:
            print("Loan feature has been enabled")
        else:
            print("Loan feature has been disabled")



def user_menu(bank):
    account_number = int(input("Enter your account number: "))
    if account_number not in bank.accounts:
        print("Account not found")
        return
    
    account = bank.accounts[account_number]

    while True:
        print("User Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer")
        print("7. Logout")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            account.check_available_balance()
        elif choice == 4:
            account.check_transaction_history()
        elif choice == 5:
            amount = int(input("Enter loan amount: "))
            account.loan_taken(amount)
        elif choice == 6:
            other_account_number = int(input("Enter other account number: "))
            if other_account_number in bank.accounts:
                other_account = bank.accounts[other_account_number]
                amount = int(input("Enter amount to transfer: "))
                account.transfer(amount, other_account)
            else:
                print("Other account not found")
        elif choice == 7:
            break
        else:
            print("Invalid choice.")

def admin_menu(bank):
    while True:
        print("Admin Menu:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. check Total Balance")
        print("5. check total loan amount")
        print("6. loan feature available")
        print("7. logout")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type (Saving/Current): ")
            bank.create_account(name, email, address, account_type)
        elif choice == 2:
            account_number = int(input("Enter account number to delete: "))
            bank.delete_account(account_number)
        elif choice == 3:
            accounts = bank.user_account_list()
            if accounts:
                for acct_number, account in accounts.items():
                    print(f"Account Number: {acct_number}, Name: {account.name}, Balance: {account.balance}")
        elif choice == 4:
            bank.check_total_balance()
        elif choice == 5:
            bank.check_total_loan_amount()
        elif choice == 6:
            bank.loan_feature_available()
        elif choice == 7:
            break
        else:
            print("Invalid choice.")

bank = Admin()

while True:
    print("1. Login Admin")
    print("2. Login User")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        admin_menu(bank)
    elif choice == 2:
        user_menu(bank)
    elif choice == 3:
        break
    else:
        print("Invalid choice.")            