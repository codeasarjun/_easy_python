def multiply(a, b):
    # intentional bug: incorrect operation
    return a + b

def divide(a, b):
    # intentional bug: division by zero
    return a / b

if __name__ == "__main__":
    print(multiply(2, 3))  # expected output: 6
    print(divide(10, 0))   # expected to raise ZeroDivisionError
