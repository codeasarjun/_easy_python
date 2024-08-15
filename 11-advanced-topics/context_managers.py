import sqlite3

class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None

    def __enter__(self):
        # open the database connection and create a cursor
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        # commit any pending transactions
        if exc_type is None:
            self.connection.commit()
        else:
            # rollback in case of an error
            self.connection.rollback()
        # close the cursor and connection
        self.cursor.close()
        self.connection.close()

# usage of the custom context manager
db_file = 'test_student.db'

# create and populate the database for demonstration purposes
def setup_database():
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Alice', 'alice@example.com'))
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Bob', 'bob@example.com'))

# function to query the database
def query_users():
    with DatabaseConnection(db_file) as cursor:
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

setup_database()
print("User Records:")
query_users()
