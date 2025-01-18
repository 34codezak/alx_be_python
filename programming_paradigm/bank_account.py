class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional initial balance (default is 0).
        """
        self._account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """
        Deposit a specified amount to the account balance.
        """
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited {amount}. Current balance: {self._account_balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account balance.
        If insufficient funds, return False. Otherwise, deduct and return True.
        """
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                print(f"Withdrew {amount}. Current balance: {self._account_balance}")
                return True
            else:
                print("Insufficient funds!")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current balance: ${self._account_balance:.2f}")
