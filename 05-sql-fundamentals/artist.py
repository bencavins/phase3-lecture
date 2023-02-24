import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

class Artist:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return f"<Artist {self.name}>"
    
    def insert(self):
        """Insert a new artist into the DB"""
        query = f"""
            INSERT INTO artists (name)
            VALUES ("{self.name}");
        """
        cursor.execute(query)
        conn.commit()
    
    def update(self):
        query = f"""
            UPDATE artists
            SET Name = "{self.name}"
            WHERE artistId = {self.id}
        """
        cursor.execute(query)
        conn.commit()
    
    def delete(self):
        query = f"""
            DELETE FROM artists
            WHERE ArtistId = {self.id};
        """
        cursor.execute(query)
        conn.commit()
    
    @classmethod
    def get_by_id(cls, id):
        query = f"""
            SELECT ArtistId, Name
            FROM artists
            WHERE ArtistId = {id};
        """
        result = cursor.execute(query).fetchone()
        new_artist = Artist(result[0], result[1])
        return new_artist
    
    @classmethod
    def create_table(cls):
        pass
    

if __name__ == '__main__':
    artist = Artist.get_by_id(1)
    artist.name = 'AC/DC!!!!!'
    artist.update()
