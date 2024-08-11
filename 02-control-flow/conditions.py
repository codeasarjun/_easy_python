def check_number(num):
    """Check if a number is positive, negative, or zero."""
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."
number = 10
print(f"Number: {number} - {check_number(number)}")

number = -5
print(f"Number: {number} - {check_number(number)}")

number = 0
print(f"Number: {number} - {check_number(number)}")
