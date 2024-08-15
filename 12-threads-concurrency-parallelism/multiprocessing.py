from multiprocessing import Pool
import time

# function to perform a time-consuming computation
def compute_square(n):
    time.sleep(1)  
    return n * n

# list of numbers to process
numbers = [1, 2, 3, 4, 5]

# creatin a pool of worker processes
with Pool(processes=4) as pool:
    results = pool.map(compute_square, numbers)

print("Results:", results)
