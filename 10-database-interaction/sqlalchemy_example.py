from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# set up the database engine and session
engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

# define a base class for declarative class definitions
Base = declarative_base()

# define the Book class
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publication_year = Column(Integer)

# creating the table
Base.metadata.create_all(engine)

# adding a new book
new_book = Book(title='To Kill a Mockingbird', author='Harper Lee', publication_year=1960)
session.add(new_book)
session.commit()

# query and display all books
books = session.query(Book).all()
for book in books:
    print(f'{book.id}: {book.title} by {book.author}, {book.publication_year}')

# close the session
session.close()
