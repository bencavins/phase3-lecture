import sqlite3

# create a connection object
con = sqlite3.connect("./chinook.db")


def get_all_artists():
    """Return all the artist data from the db"""
    # create a string for our query
    sql = """
        SELECT * 
        FROM artists
    """
    # create a cursor
    cursor = con.cursor()
    # execute our sql
    cursor = cursor.execute(sql)
    return cursor.fetchall()

def get_artist_by_id(id):
    """Returns the row of the artist with the matching id"""
    sql = f"""
        SELECT *
        FROM artists
        WHERE ArtistId = ?
    """
    cursor = con.cursor()
    cursor.execute(sql, [id])  # puts "id" where the ? is
    return cursor.fetchone()


def add_artist(name):
    sql = """
        INSERT INTO artists
        (Name)
        VALUES
        (?)
    """
    cursor = con.cursor()
    cursor.execute(sql, (name,))
    # commit our changes to the db
    con.commit()


def update_artist_name_by_id(id, new_name):
    sql = """
        UPDATE artists
        SET Name = ?
        WHERE ArtistId = ?
    """
    cursor = con.cursor()
    cursor.execute(sql, [new_name, id])
    con.commit()


if __name__ == '__main__':
    print(update_artist_name_by_id(276, 'NEW TEST NAME'))
