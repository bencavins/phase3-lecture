from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
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


if __name__ == '__main__':
    engine = create_engine('sqlite:///chinook.db')
    with Session(engine) as session:
        all_artists = session.query(
            Artist
        ).order_by(Artist.name.desc()).all()
        print(all_artists)
