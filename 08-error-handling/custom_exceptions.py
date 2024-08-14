class AccountError(Exception):
    """Base class for other custom exceptions related to accounts"""
    pass

class InsufficientFundsError(AccountError):
    """Raised when there are not enough funds for a transaction"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Balance is ${balance}, but attempted to withdraw ${amount}")

class InvalidAmountError(AccountError):
    """Raised when the amount for a transaction is invalid"""
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Invalid amount: ${amount}. The amount must be greater than zero.")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

account = BankAccount(1000)

try:
    print("Initial balance:", account.get_balance())  # Output: 1000
    print("Depositing $500...")
    account.deposit(500)
    print("Balance after deposit:", account.get_balance())  # Output: 1500

    print("Withdrawing $2000...")
    account.withdraw(2000)  # Should raise InsufficientFundsError
except AccountError as e:
    print(e)

try:
    print("Withdrawing $-100...")
    account.withdraw(-100)  # will raise InvalidAmountError
except AccountError as e:
    print(e)

print("Final balance:", account.get_balance())  # Output will depend on previous transactions
