import sqlite3
from artist import Artist

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

class Album:
    def __init__(self, id, title, artist_id):
        self.id = id
        self.title = title
        self.artist_id = artist_id
        self.artist = None
    
    def __repr__(self) -> str:
        return f"<Album {self.title} by {self.artist.name}>"
    
    @classmethod
    def get_by_id(cls, id):
        query = f"""
            SELECT AlbumId, Title, ArtistId
            FROM albums
            WHERE AlbumId = {id};
        """
        result = cursor.execute(query).fetchone()
        album = Album(result[0], result[1], result[2])
        artist = Artist.get_by_id(result[2])
        album.artist = artist
        return album


if __name__ == '__main__':
    album = Album.get_by_id(1)
    print(album)
    # print(album.artist)