
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    else:
        return result

def access_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print("Error: Index out of range.")
        return None


print(divide_numbers(10, 2))  
print(divide_numbers(10, 0))  # will print an error message
print(access_list_element([1, 2, 3], 5))  # will print an error message
