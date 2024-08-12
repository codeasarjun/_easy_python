
global_var = "I'm a global variable" # a global variable

def my_function():
    
    local_var = "I'm a local variable" # Local variable
    print(global_var)  # accessing global variable
    print(local_var)   # accessing local variable


my_function() # calling funtion

# This will raise an error because local_var is not accessible outside the function
# print(local_var)  # uncommenting this line will cause an error
