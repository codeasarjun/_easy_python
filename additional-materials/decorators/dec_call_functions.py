
from decorators_example import log_function_call, timing_decorator, requires_authentication, cache_results, rate_limit

@log_function_call
def add(a, b):
    return a + b

@timing_decorator
def compute_square(n):
    return [i ** 2 for i in range(n)]

@requires_authentication
def view_profile(user):
    return f"Welcome to your profile, {user['name']}!"

@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@rate_limit(max_calls=1, period=5)
def fetch_data():
    return "Data fetched successfully!"
