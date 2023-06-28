from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    author = Column(String(), nullable=False)

    def __repr__(self):
        return f"<Book {self.title} {self.author}>"

if __name__ == '__main__':
    engine = create_engine('sqlite:///books.db')
    # Create db tables
    # Base.metadata.create_all(engine)

    # Get the db session
    Session = sessionmaker(bind=engine)
    session = Session()


    # Create some book objs
    b1 = Book(
        id=1, 
        title='Grapes of Wrath', 
        author='Steinbeck'
    )
    session.add(b1)
    session.commit()
