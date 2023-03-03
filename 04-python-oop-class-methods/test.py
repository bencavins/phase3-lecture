import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()


if __name__ == '__main__':
    # title = 'Jagged Little Pill'
    title = """ "; DROP TABLE albums; -- """
    query = f"""
    select * 
    from albums
    where title = "{title}";
    """
    res = cursor.execute(query).fetchone()
    print(res)
