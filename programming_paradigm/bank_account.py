class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional starting balance."""
        self.__account_balance = initial_balance  # Private attribute for encapsulation

    def deposit(self, amount):
        """Add the specified amount to the balance."""
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited: ${amount:.2f}"
        return "Error: Deposit amount must be greater than zero."

    def withdraw(self, amount):
        """Withdraw the amount if sufficient balance is available."""
        if amount <= 0:
            return "Error: Withdrawal amount must be greater than zero."
        elif amount > self.__account_balance:
            return f"Error: Insufficient funds. Available balance: ${self.__account_balance:.2f}"
        else:
            self.__account_balance -= amount
            return f"Withdrew: ${amount:.2f}"

    def display_balance(self):
        """Return the current balance in a user-friendly format."""
        return f"Current Balance: ${self.__account_balance:.2f}"
