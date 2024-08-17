# a lambda function to add two numbers
add = lambda x, y: x + y

# a lambda function to check if a number is even
is_even = lambda x: x % 2 == 0

square = lambda x: x * x

if __name__ == "__main__":
    print(f"Add 5 and 3: {add(5, 3)}")           
    print(f"Is 4 even? {'Yes' if is_even(4) else 'No'}")  
    print(f"Square of 7: {square(7)}")
