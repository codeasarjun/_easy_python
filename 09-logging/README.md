## Overview

### Logger

A logger is a component in Python's `logging` module used to record log messages. It provides a way to capture and record messages with various levels of severity (DEBUG, INFO, WARNING, ERROR, CRITICAL).
 Loggers can be configured to output these messages to different destinations, such as the console or log files, and with different formats.

**Key Components:**

- **Log Level**: Defines the severity of the messages that the logger will handle. Examples include DEBUG, INFO, WARNING, ERROR, and CRITICAL.
- **Handler**: Determines where the log messages go, such as the console or a file.
- **Formatter**: Specifies the format of the log messages, including the layout and details such as timestamps and log levels.


## Scripts

### `logging_example.py`

This script demonstrates how to configure logging in Python using the `logging` module. It logs messages to both the console and a file named `test_log.log`.

**Features:**
- Logs messages with different severity levels: DEBUG, INFO, WARNING, ERROR.
- Outputs logs to the console and a file.


### monitoring_example.py

This script monitors the `test_log.log` file for new log entries and prints them to the console in real-time.

**Features:**

- Continuously checks the `test_log.log` file.
- Prints new log entries as they are added.




