from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    author_id = Column(Integer(), ForeignKey('authors.id'))

    def __repr__(self):
        return f"<Book {self.title}>"

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    books = relationship('Book', backref='author')

    def __repr__(self):
        return f"<Author {self.name}>"

if __name__ == '__main__':
    engine = create_engine('sqlite:///books.db')
    # Create db tables
    Base.metadata.create_all(engine)

    # Get the db session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create some book objs
    b1 = Book(title='Grapes of Wrath')
    b2 = Book(title='East of Eden', author_id=1)
    # a1 = Author(name='John Steinbeck')
    # b1.author = a1

    # session.add(b2)
    # session.add(a1)
    # session.commit()
