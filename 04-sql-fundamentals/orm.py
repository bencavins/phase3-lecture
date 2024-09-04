# ORM == Object Relational Mapper
# Map relational database rows to Python objects
# sqlalchemy

import sqlite3

conn = sqlite3.connect("chinook.db")


class Artist:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
    
    @classmethod
    def create_table(cls):
        # runs create table query
        pass

    @classmethod
    def get_artist_by_id(cls, id):
        """Query db for an artist with this id, return an artist obj"""
        
        sql = f"""
            SELECT ArtistId, Name
            FROM artists
            WHERE ArtistId = {id}
        """
        cursor = conn.cursor()
        row = cursor.execute(sql).fetchone()
        
        artist_obj = Artist(id=row[0], name=row[1])
        return artist_obj
    
    @classmethod
    def get_all_artists(cls):
        """Query db for all artists, return an array of artist objects"""

        sql = """
            SELECT ArtistId, Name
            FROM artists
        """
        cursor = conn.cursor()
        result = []
        for row in cursor.execute(sql):
            artist_obj = Artist(id=row[0], name=row[1])
            result.append(artist_obj)
        return result
    
    def insert(self):
        """Insert this artist into the db"""

        insert_sql = """
            INSERT INTO artists (Name)
            VALUES (?)
        """
        cursor = conn.cursor()
        cursor.execute(insert_sql, [self.name])
        self.id = cursor.lastrowid  # get the db id, add it to the obj
        conn.commit()

    def update(self):
        """Update this artist in the database"""

        # sql = f"""
        #     UPDATE artists
        #     SET Name = "{self.name}"
        #     WHERE ArtistId = {self.id}
        # """
        sql = """
            UPDATE artists
            SET Name = ?
            WHERE ArtistId = ?
        """
        cursor = conn.cursor()
        cursor.execute(sql, [self.name, self.id])
        conn.commit()

    def save(self):
        """Insert or update this artist"""
        if self.id is None:
            self.insert()
        else:
            self.update()

    def delete(self):
        # run delete query
        # commit
        self.id = None

    
    def __repr__(self) -> str:
        return f'<Artist {self.id} {self.name}>'


if __name__ == '__main__':
    # artists = [
        # Artist.get_artist_by_id(281),
    #     Artist.get_artist_by_id(282),
    #     Artist(name='something'),
    #     Artist(name='something else'),
    # ]

    # artists[0].name = 'xyz'
    # artists[1].name = 'hello'

    # for artist in artists:
    #     artist.save()

    a = Artist(name='test', id=1)
    a.save()
