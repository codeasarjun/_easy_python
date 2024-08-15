import time
import os

log_file_path = os.path.join(os.path.dirname(__file__), 'test_log.log')

def monitor_log_file(file_path):
    with open(file_path, 'r') as file:
        file.seek(0, os.SEEK_END)  # moving the pointer to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  # waiting before checking for new lines again
                continue
            print(f'New log entry: {line.strip()}')

if __name__ == '__main__':
    monitor_log_file(log_file_path)
