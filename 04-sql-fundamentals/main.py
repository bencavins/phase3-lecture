import sqlite3

connection = sqlite3.connect("chinook.db")  # connect to db
cursor = connection.cursor()  # get the cursor
# results = cursor.execute('SELECT * FROM artists').fetchall()  # execute query
# # or
# result_cursor = cursor.execute('SELECT * FROM artists')
# for row in result_cursor:
#     print(row)

new_artist = input("Enter a new artist: ")

sql = """
INSERT INTO artists (Name)
VALUES
(:name)
"""

cursor.executemany(sql, [{'name': new_artist}])  # prevents sql injection attacks

connection.commit()  # commit the transactions (save to db)