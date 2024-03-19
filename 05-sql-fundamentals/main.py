import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

id = input('Enter an id: ')
print(id)

query = f"""
SELECT ArtistId, Name
FROM artists
WHERE ArtistId = {id};
"""

result = cursor.execute(query)
print(result.fetchone())