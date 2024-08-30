# decorators.py

import time
import logging
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute")
        return result
    return wrapper

def requires_authentication(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get('authenticated'):
            return "Access Denied: User not authenticated"
        return func(user, *args, **kwargs)
    return wrapper

def cache_results(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result
    return wrapper

def rate_limit(max_calls, period):
    def decorator(func):
        last_called = [0]
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            if current_time - last_called[0] < period:
                return "Rate limit exceeded. Please try again later."
            last_called[0] = current_time
            return func(*args, **kwargs)
        return wrapper
    return decorator
