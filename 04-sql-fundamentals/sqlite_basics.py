import sqlite3

# create database connection
conn = sqlite3.connect("chinook.db")

# create a cursor
cursor = conn.cursor()


if __name__ == '__main__':
    sql = "SELECT ArtistId, Name FROM artists"

    result_cursor = cursor.execute(sql)  # run a query, fetch result
    
    # grab one single row
    row = result_cursor.fetchone()

    # grab all rows all at once
    all_results = result_cursor.fetchall()

    # can iterate over the execute cursor
    for row in cursor.execute(sql):
        print(row)
    
    # prompt user for artist
    artist = input('Enter an artist: ')
    data = [[artist]]

    # insert artist (sanitize input data)
    insert_sql = f"""
        INSERT INTO artists (Name)
        VALUES (?)
    """
    cursor.executemany(insert_sql, data)

    # commit your changes
    conn.commit()
    
