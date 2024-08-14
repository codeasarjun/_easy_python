File handling is an essential concept in programming that allows you to read from and write to files on your computer.

## What is File Handling?

File handling refers to the process of performing operations on files stored in a computer’s file system. It allows you to:

- **Create** new files
- **Read** data from existing files
- **Write** data to files
- **Append** new data to existing files
- **Delete** files

These operations are fundamental for storing and retrieving data in many applications.

- `read_write_files.py`: A Python script that demonstrates how to perform basic file operations.


## Basic File Operations

### 1. Writing to a File

To create a file and write data to it, use the `write_to_file` function. This function takes two arguments:

- `filename`: The name of the file to which data will be written.
- `content`: The text data that will be written to the file.

When we call this function, it opens the file in write mode. If the file doesn’t exist, it creates a new one. If it does exist, the existing content is overwritten.

Example usage:

```python
write_to_file('example.txt', 'This is some sample text.')
```

