import time

# Account database (File simulation)
accounts = {
    "12345": {"pin": "1234", "balance": 10000, "transactions": []},
    "67890": {"pin": "5678", "balance": 5000, "transactions": []}
}

# Save transaction history
def record_transaction(account, message):
    accounts[account]["transactions"].append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

# ATM Class
class ATM:
    def __init__(self):
        self.current_account = None

    def authenticate(self):
        print("\n---- Welcome to Python ATM ----")
        account = input("Enter your account number: ")
        if account in accounts:
            pin = input("Enter your PIN: ")
            if accounts[account]["pin"] == pin:
                self.current_account = account
                print("Login successful!\n")
                return True
            else:
                print("Incorrect PIN.")
        else:
            print("Account not found.")
        return False

    def display_balance(self):
        balance = accounts[self.current_account]["balance"]
        print(f"\nYour current balance is: ₹{balance}")
        record_transaction(self.current_account, f"Checked balance: ₹{balance}")

    def withdraw_cash(self):
        amount = float(input("\nEnter the amount to withdraw: ₹"))
        if amount > accounts[self.current_account]["balance"]:
            print("Insufficient balance!")
        else:
            accounts[self.current_account]["balance"] -= amount
            print(f"₹{amount} withdrawn successfully!")
            self.display_balance()
            record_transaction(self.current_account, f"Withdrawn: ₹{amount}")

    def deposit_cash(self):
        amount = float(input("\nEnter the amount to deposit: ₹"))
        accounts[self.current_account]["balance"] += amount
        print(f"₹{amount} deposited successfully!")
        self.display_balance()
        record_transaction(self.current_account, f"Deposited: ₹{amount}")

    def transfer_funds(self):
        target_account = input("\nEnter the account number to transfer funds: ")
        if target_account in accounts and target_account != self.current_account:
            amount = float(input("Enter the amount to transfer: ₹"))
            if amount > accounts[self.current_account]["balance"]:
                print("Insufficient balance!")
            else:
                accounts[self.current_account]["balance"] -= amount
                accounts[target_account]["balance"] += amount
                print(f"₹{amount} transferred successfully to account {target_account}!")
                self.display_balance()
                record_transaction(self.current_account, f"Transferred ₹{amount} to account {target_account}")
                record_transaction(target_account, f"Received ₹{amount} from account {self.current_account}")
        else:
            print("Invalid account number!")

    def show_transaction_history(self):
        print("\n--- Transaction History ---")
        transactions = accounts[self.current_account]["transactions"]
        if transactions:
            for t in transactions:
                print(t)
        else:
            print("No transactions available.")

    def logout(self):
        print("\nThank you for using Python ATM. Goodbye!")
        self.current_account = None

    def run(self):
        while True:
            print("\n1. Balance Inquiry")
            print("2. Withdraw Cash")
            print("3. Deposit Cash")
            print("4. Transfer Funds")
            print("5. Transaction History")
            print("6. Exit")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.display_balance()
            elif choice == "2":
                self.withdraw_cash()
            elif choice == "3":
                self.deposit_cash()
            elif choice == "4":
                self.transfer_funds()
            elif choice == "5":
                self.show_transaction_history()
            elif choice == "6":
                self.logout()
                break
            else:
                print("Invalid choice! Please try again.")

# Main Program
if __name__ == "__main__":
    atm = ATM()
    if atm.authenticate():
        atm.run()
