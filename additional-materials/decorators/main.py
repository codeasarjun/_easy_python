import time
from dec_call_functions import add, compute_square, view_profile, fibonacci, fetch_data

if __name__ == "__main__":
    print(add(5, 7))
    compute_square(1000000)
    user1 = {'name': 'Alice', 'authenticated': True}
    user2 = {'name': 'Bob', 'authenticated': False}
    print(view_profile(user1))
    print(view_profile(user2))
    print(fibonacci(10))
    print(fetch_data())
    time.sleep(3)
    print(fetch_data())
    time.sleep(5)
    print(fetch_data())
