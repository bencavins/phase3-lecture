import sqlite3

# create a connection to db
conn = sqlite3.connect('chinook.db')

# get a cursor to communicate with db
cursor = conn.cursor()

# run a select query
result = cursor.execute('SELECT * FROM artists')

# get one row (returns tuple)
row = result.fetchone()

# get all rows (returns list of tuples)
rows = result.fetchall()

id = input('enter an id: ')
artist = input('enter an artist: ')
# 'Lady Gaga'); DROP TABLE artists; 

# insert data into db
# be careful of sqlinjection attacks
# query = f"INSERT INTO artists VALUES ({id}, 'Lady Gaga'); DROP TABLE artists; ')"
# # print(query)
# cursor.execute(f"INSERT INTO artists VALUES ({id}, '{artist}')")
data = [
    (id, artist)
]
cursor.executemany("INSERT INTO artists VALUES (?, ?)", data)

# need to commit in order to persist changes
conn.commit()

# throw away all changes since last commit
conn.rollback()

# close your connection
conn.close()