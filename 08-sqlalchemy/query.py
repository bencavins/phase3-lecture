from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from book import Book

if __name__ == '__main__':
    engine = create_engine('sqlite:///books.db')

    # Get the db session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get all the book rows
    all_books = session.query(Book).all()

    one_book = session.query(Book).filter(
        Book.id != 1
    ).one()

    # Update a book
    all_books[0].author = 'John Stenbeck'

    # save and commit
    session.add(all_books) # a single obj
    session.add_all(all_books) # multiple objs
    session.commit()

