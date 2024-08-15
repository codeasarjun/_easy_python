import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

# using the decorator
@timing_decorator
def slow_function(seconds):
    time.sleep(seconds)
    print("Function completed")

# testintg the decorated function
slow_function(2)
