from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session

Base = declarative_base()

class Artist(Base):
    artistId = Column(Integer(), primary_key=True)
    name = Column(String())


if __name__ == '__main__':
    engine = create_engine('sqlite:///chinook.db')
    Base.metadata.create_all(engine)

    # session = Session(engine)
    with Session(engine) as session:
        pass