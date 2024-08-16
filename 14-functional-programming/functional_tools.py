from functools import reduce

def square(x):
    return x * x

#add two numbers (used in reduce)
def add(x, y):
    return x + y

# map function to apply 'square' to a list of numbers
def square_numbers(numbers):
    return list(map(square, numbers))

# filter function to keep only even numbers from a list
def filter_even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

# reduce function to sum all numbers in a list
def sum_numbers(numbers):
    return reduce(add, numbers)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    squared_numbers = square_numbers(numbers)
    even_numbers = filter_even(numbers)
    total_sum = sum_numbers(numbers)
    
    print(f"Squared numbers: {squared_numbers}")       
    print(f"Even numbers: {even_numbers}")             
    print(f"Sum of numbers: {total_sum}")
