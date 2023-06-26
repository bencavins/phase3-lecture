import sqlite3

query = '''
select ArtistId, Name
from artists;
'''

def get_connection():
    return sqlite3.connect('chinook.db')

if __name__ == '__main__':
    conn = get_connection()
    cursor = conn.cursor()
    results = cursor.execute(query).fetchall()

    for row in results:
        print(row[0], row[1])

    conn.close()