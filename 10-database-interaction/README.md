
This repo demonstrates how to interact with an SQLite database using two different approaches in Python:

1. Directly using SQLite with the `sqlite3` module.
2. Using SQLAlchemy, an Object-Relational Mapping (ORM) library.

## Project Structure

The project contains the following files:

- `sqlite_example.py`: A Python script demonstrating basic SQLite database operations.
- `sqlalchemy_example.py`: A Python script demonstrating database operations using SQLAlchemy ORM.
- `README.md`: This file, providing an overview and instructions for using the examples.

## Setup

Before running the examples, ensure you have Python installed on your system. You will also need to install SQLAlchemy if you plan to use the `sqlalchemy_example.py` script. You can install it using pip:

```sh
pip install sqlalchemy
```

## SQLite Example

`sqlite_example.py` demonstrates how to perform basic database operations using SQLite directly.

### Create the Database and Table

- The script will create a file named `library.db` in the same directory.
- It will create a table named `books` with columns for `id`, `title`, `author`, and `publication_year`.

### Insert Data

- The script inserts a sample book into the `books` table.

### Query Data

- It retrieves and prints all entries in the `books` table.

