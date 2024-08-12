
def apply_function(func, value): #function that takes another function as an argument
    return func(value)


def square(x):
    return x * x

def double(x):
    return x * 2

number = 4
print(f"The square of {number} is {apply_function(square, number)}")
print(f"The double of {number} is {apply_function(double, number)}")


def make_multiplier(factor): # function that returns another function
    def multiplier(x):
        return x * factor
    return multiplier

times_three = make_multiplier(3)
print(f"5 times 3 is {times_three(5)}")
