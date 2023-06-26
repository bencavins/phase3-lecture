from main import get_connection

query = '''
insert into artists
(Name)
values
("Van Halen")
'''

conn = get_connection()
cursor = conn.cursor()

# no fetch needed when writing data
cursor.execute(query)

print(cursor.execute('select * from artists where name = "Van Halen"').fetchall())

# need to commit after writing data
conn.commit()