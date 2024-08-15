import sqlite3

# connecting to SQLite database
conn = sqlite3.connect('library.db')

# creating a cursor object to execute SQL commands
cursor = conn.cursor()

# creating a table for storing books
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    publication_year INTEGER
)
''')

# inserting a new book into the table
cursor.execute('''
INSERT INTO books (title, author, publication_year)
VALUES (?, ?, ?)
''', ('To Kill a Mockingbird', 'Harper Lee', 1960))

# committing the transaction
conn.commit()

# quer and display all books
cursor.execute('SELECT * FROM books')
books = cursor.fetchall()
for book in books:
    print(book)

# close the connection
conn.close()
