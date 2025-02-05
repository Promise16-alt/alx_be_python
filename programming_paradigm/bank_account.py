class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional starting balance."""
        self.__account_balance = initial_balance  # Encapsulation for security

    def deposit(self, amount):
        """Add the specified amount to the balance."""
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited: ${amount:.2f}"
        return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        """Withdraw the amount if sufficient balance is available."""
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        elif amount > self.__account_balance:
            return "Insufficient funds."
        else:
            self.__account_balance -= amount
            return f"Withdrew: ${amount:.2f}"

    def display_balance(self):
        """Return the current balance in a user-friendly format."""
        return f"Current Balance: ${self.__account_balance:.2f}"
