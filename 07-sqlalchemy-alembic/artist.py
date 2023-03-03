from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'

    artistId = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"<Artist id={self.artistId} name={self.name}>"


def add_new_obj():
    # create db engine
    engine = create_engine('sqlite:///chinook.db')

    # create schema
    Base.metadata.create_all(engine)

    # session = Session(engine)
    with Session(engine) as session:
        # create a new artist obj
        my_artist = Artist(
            name='Metallica!!!'
        )
        # add it to the db session
        session.add(my_artist)
        # commit changes
        session.commit()
        print(my_artist)

    # leave the with clause, cleanup happens


def select():
    """
    If we query for the whole Artist, we will be back
    Artist objects. If we query for a column (for 
    example: Artist.name) we will get tuples back
    """
    engine = create_engine('sqlite:///chinook.db')
    with Session(engine) as session:
        all_artists = session.query(Artist).all()
        print(all_artists)


def order_by():
    engine = create_engine('sqlite:///chinook.db')
    with Session(engine) as session:
        all_artists = session.query(
            Artist
        ).order_by(Artist.name.desc()).all()
        print(all_artists)

def limit():
    engine = create_engine('sqlite:///chinook.db')
    with Session(engine) as session:
        result = session.query(Artist).limit(1).all()
        print(result)

def filter_by():
    engine = create_engine('sqlite:///chinook.db')
    with Session(engine) as session:
        result = session.query(Artist).filter(Artist.name == 'Metallica').all()
        print(result)

def bulk_update():
    engine = create_engine('sqlite:///chinook.db')
    with Session(engine) as session:
        artist = session.query(Artist).update({Artist.name: Artist.name + '!'})
        # session.add(artist)
        session.commit()

def delete():
    engine = create_engine('sqlite:///chinook.db')
    with Session(engine) as session:
        artist = session.query(Artist).filter(
            Artist.name == 'Metallica!!!!'
        ).first()
        # print(artist)
        session.delete(artist)
        session.commit()


if __name__ == '__main__':
    engine = create_engine('sqlite:///chinook.db')
    with Session(engine) as session:
        artist = session.query(Artist).filter(
            Artist.name == 'Metallica!'
        ).all()
        print(artist)
        # session.delete(artist)
        # session.commit()
