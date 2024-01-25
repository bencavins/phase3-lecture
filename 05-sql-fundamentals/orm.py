# ORM -- Object Relational Mapper
# SQLAlchemy will be used later

import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

class Artist:
    pass

class Album:
    def __init__(self, title, artist_id, id=None):
        self.id = id
        self.title = title
        self.artist_id = artist_id
    
    @classmethod
    def get_by_id(cls, id):
        sql = """
            SELECT AlbumId, Title, ArtistId
            FROM albums
            WHERE AlbumId = ?
        """
        row = cursor.execute(sql, [id]).fetchone()
        return Album(id=row[0], title=row[1], artist_id=row[2])
    
    @classmethod
    def get_all_albums(cls):
        sql = """
            SELECT AlbumId, Title, ArtistId
            FROM albums
        """
        albums = []
        for row in cursor.execute(sql):
            albums.append(Album(id=row[0], title=row[1], artist_id=row[2]))
        return albums
    
    def update(self):
        sql = """
            UPDATE albums 
            SET Title = ?, ArtistId = ? 
            WHERE AlbumId = ?
        """
        cursor.execute(sql, [self.title, self.artist_id, self.id])
        conn.commit()

    def insert(self):
        sql = """
            INSERT INTO albums (Title, ArtistId)
            VALUES (?, ?)
        """
        result = cursor.execute(sql, [self.title, self.artist_id])
        self.id = result.lastrowid
        conn.commit()
    
    def save(self):
        if self.id is None:
            self.insert()
        else:
            self.update()
    
    def __repr__(self) -> str:
        return f"<Album {self.title}>"


if __name__ == '__main__':
    album = Album(title='Let Go', artist_id=1)
    album.save()