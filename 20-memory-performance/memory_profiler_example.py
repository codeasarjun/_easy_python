from memory_profiler import profile
import time

@profile
def compute_sum(n):
    total = 0
    for i in range(n):
        total += i
        time.sleep(0.01)  # some delay
    return total

if __name__ == "__main__":
    result = compute_sum(1000)
    print(f"Sum is {result}")
