## What Are Exceptions?

In programming, exceptions are special conditions or errors that occur during the execution of a program. They disrupt the normal flow of a program and require special handling to ensure the program can continue running or terminate gracefully.

### Types of Exceptions in Python

Python has several built-in exception types that represent different error conditions:

- **`Exception`**: The base class for all built-in exceptions. Custom exceptions should inherit from this class.
- **`ValueError`**: Raised when a function receives an argument of the right type but inappropriate value.
- **`TypeError`**: Raised when an operation or function is applied to an object of inappropriate type.
- **`IndexError`**: Raised when trying to access an index that is out of range in a list or other sequence types.
- **`KeyError`**: Raised when trying to access a dictionary with a key that doesn’t exist.
- **`ZeroDivisionError`**: Raised when dividing a number by zero.

## Files
1. `basic_exceptions.py`: Covers handling built-in exceptions.
2. `custom_exceptions.py`: Shows how to create and use custom exceptions.

### `basic_exceptions.py`

This script demonstrates handling Python's built-in exceptions with practical examples:

- **`divide_numbers(num1, num2)`**: Divides two numbers and handles:
  - **`ZeroDivisionError`**: When dividing by zero.
  - **`TypeError`**: When the arguments are not numbers.

- **`access_list_element(my_list, index)`**: Accesses an element in a list and handles:
  - **`IndexError`**: When the index is out of range.


### `custom_exceptions.py`

This script includes:

1. **Custom Exceptions**: Defined to handle specific errors related to account management.
2. **BankAccount Class**: Manages an account's balance with deposit and withdrawal methods.

#### Custom Exceptions

- **AccountError**: Base class for all custom exceptions related to accounts.
- **InsufficientFundsError**: Raised when an attempt is made to withdraw more money than the account balance.
- **InvalidAmountError**: Raised when a transaction amount is invalid (e.g., negative or zero).

#### BankAccount Class

- **`__init__(self, balance)`**: Initializes the bank account with a starting balance.
- **`deposit(self, amount)`**: Adds money to the account. Raises `InvalidAmountError` if the amount is not positive.
- **`withdraw(self, amount)`**: Removes money from the account. Raises `InsufficientFundsError` if there are insufficient funds or `InvalidAmountError` if the amount is not positive.
- **`get_balance(self)`**: Returns the current account balance.

