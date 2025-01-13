# ORM == Object Relational Mapper
# SQLAlchemy

import sqlite3

connection = sqlite3.connect('chinook.db')
# cursor = connection.cursor()


class Artist:

    @classmethod
    def get_by_id(cls, id):
        """Query the db for artist with id, return an Artist object"""
        sql = """
            SELECT ArtistId, Name 
            FROM artists 
            WHERE ArtistId = ?"""
        cursor = connection.cursor()
        row = cursor.execute(sql, [id]).fetchone()
        print(row)
        return Artist(id=row[0], name=row[1])

    @classmethod
    def get_all(cls):
        """Query db for all artists, return list of objects"""
        sql = """
            SELECT ArtistId, Name
            FROM artists"""
        artists = []
        cursor = connection.cursor()
        for row in cursor.execute(sql):
            artist = Artist(id=row[0], name=row[1])  # turn db row into Artist object
            artists.append(artist)
        return artists

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError('name cannot be empty')

    def insert(self):
        """Inserts this artist object into the db"""
        sql = f"""
            INSERT INTO artists (Name) 
            VALUES (?)"""
        cursor = connection.cursor()
        result = cursor.execute(sql, [self.name])
        self.id = result.lastrowid  # grab the id the db created for us
        connection.commit()
    
    def update(self):
        """Updates an existing artist in the db"""
        sql = """
            UPDATE artists 
            SET Name = ? 
            WHERE ArtistId = ?"""
        cursor = connection.cursor()
        cursor.execute(sql, [self.name, self.id])
        connection.commit()
    
    def save(self):
        """Inserts or updates the artist in the db"""
        if self.id is None:
            self.insert()
        else:
            self.update()
    
    def delete(self):
        """Deletes the artist from the db"""
        sql = """
            DELETE FROM Artists
            WHERE ArtistId = ?"""
        cursor = connection.cursor()
        cursor.execute(sql, [self.id])
        self.id = None
        connection.commit()
    
    def __repr__(self) -> str:
        return f"<Artist id={self.id} name={self.name}>"


if __name__ == '__main__':
    pass
    # artist = Artist(name='abc')
    # # artist.name = 'AC/DC'
    # artist.save()

    # for a in Artist.get_all():
    #     print(a)
