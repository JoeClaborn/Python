# Joe Claborn - CS1160 - Lab 09

# This program simulates a bank account manager for 2 bank accounts.
# It uses attributes and methods for the BankAccount class to get the
# internals of the program to work correctly. The user is able to
# deposit, withdrawal, check the balance of an account, list all accounts
# and exit the program.

# Bank Account class that holds an account number, bank holder's name, and balance
# within the account.
class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    # Method for depositing funds into an account.
    def deposit(self, amount):
        # If-else check to see if the deposit amount is positive.
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Method for withdrawaling funds from an account.
    def withdraw(self, amount):
        # If-else check to see if the withdrawal amount is positive and if the balance in the
        # account is greater than amount.
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    # Method to get the balance of the chosen account.
    def get_balance(self):
        return self.__balance

    # Method to get the account number of the chosen account.
    def get_account_number(self):
        return self.__account_number

    # Method to get the account holder's name of the chosen account.
    def get_holder_name(self):
        return self.__holder_name

    # Method to display the bank account info of the chosen account.
    def display_account_info(self):
        print(f"Account Number: {self.__account_number}, Holder Name: {self.__holder_name}, Balance: ${self.__balance}")

# Bank class that has an accounts list to give a unique number to a bank account.
class Bank:
    def __init__(self):
        self.__accounts = {}

    # Method for adding a bank account object to the banking system.
    def add_account(self, account):
        self.__accounts[account.get_account_number()] = account

    # Method for getting the chosen bank account within the system. Done by
    # retrieving a 'BankAccount' object by the account number.
    def get_account(self, account_number):
        return self.__accounts.get(account_number, None)

    # Method for listing the accounts when the option is chosen. This lists all the
    # accounts within the bank system.
    def list_accounts(self):
        print("List of Accounts:")
        for acc in self.__accounts.values():
            print(f"Account Number: {acc.get_account_number()}, Holder Name: {acc.get_holder_name()}")

    # Method for displaying specific account info when needed.
    def display_account_info(self, account_number):
        account = self.get_account(account_number)
        if account:
            account.display_account_info()
        else:
            print("Account not found.")

# Main workings of the program (what is displayed to the user for user input choices and outputs based upon a given choice).
# Also handles invalid inputs alongside the invald input handling in the methods above.
def main():
    bank = Bank()

    # Create some default accounts
    bank.add_account(BankAccount("001", "Alice"))
    bank.add_account(BankAccount("002", "Bob"))

    while True:
        print("\nBank Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. List Accounts")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            acc_num = input("Enter account number: ").strip()
            account = bank.get_account(acc_num)
            if account:
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid amount entered.")
            else:
                print("Account not found.")

        elif choice == "2":
            acc_num = input("Enter account number: ").strip()
            account = bank.get_account(acc_num)
            if account:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid amount entered.")
            else:
                print("Account not found.")

        elif choice == "3":
            acc_num = input("Enter account number: ").strip()
            account = bank.get_account(acc_num)
            if account:
                print(f"Account balance for {account.get_holder_name()}: ${account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == "4":
            bank.list_accounts()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
