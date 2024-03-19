# ORM -- Object Relational Mapper

import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()


class Artist:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @classmethod
    def get_by_id(cls, id):
        """Query the db for and artist with this id, build and Artist obj"""
        query = f"""
            SELECT ArtistId, Name
            FROM artists
            WHERE ArtistId = {id};
        """
        row = cursor.execute(query).fetchone()
        new_artist = Artist(name=row[1], id=row[0])
        return new_artist
    
    @classmethod
    def get_all(cls):
        """Query db for all artists, build a list of Artist objs"""
        query = """
            SELECT ArtistId, Name
            FROM artists;
        """
        artists = []
        for row in cursor.execute(query):  # by looping over cursor, fetchone gets called
            new_artist = Artist(id=row[0], name=row[1])
            artists.append(new_artist)
        return artists
    
    def insert(self):
        """Insert this artist object into the db"""
        query = """
            INSERT INTO artists (Name)
            VALUES (?)
        """
        cursor.execute(query, [self.name])
        conn.commit()
        self.id = cursor.lastrowid  # grab the new id from the db
    
    def update(self):
        """Update this artist in the db"""
        query = """
            UPDATE artists
            SET Name = ?
            WHERE ArtistId = ?
        """
        cursor.execute(query, [self.name, self.id])
        conn.commit()

    def save(self):
        if self.id is None:
            self.insert()
        else:
            self.update()

    def __repr__(self) -> str:
        return f"<Artist {self.id} {self.name}>"
    

# name = input('Enter name for new artist: ')

artists = []
existing_artist = Artist.get_by_id(284)
artists.append(existing_artist)
new_artist = Artist(name='test')
artists.append(new_artist)

for artist in artists:
    artist.name = 'testABC'
    artist.save()
