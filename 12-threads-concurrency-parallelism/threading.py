import threading
import time

# function to print numbers with a delay
def print_numbers(thread_name, start, end, delay):
    for i in range(start, end):
        print(f"{thread_name}: {i}")
        time.sleep(delay)

# function to create and start threads
def main():
    # list of threads
    threads = [
        threading.Thread(target=print_numbers, args=("Thread-1", 1, 5, 1)),
        threading.Thread(target=print_numbers, args=("Thread-2", 5, 10, 0.5)),
        threading.Thread(target=print_numbers, args=("Thread-3", 10, 15, 0.2))
    ]

    # starting all threads
    for thread in threads:
        thread.start()

    # wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All threads have finished.")

if __name__ == "__main__":
    main()
