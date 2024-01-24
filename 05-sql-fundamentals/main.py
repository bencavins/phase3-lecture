import sqlite3


conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

def do_select():
    select_query = """
    SELECT name, ArtistId
    FROM artists
    ORDER BY name
    """

    # option 1
    for row in cursor.execute(select_query):
        print(row)

    # option 2
    # result = cursor.execute(select_query).fetchall()
    # for row in result:
    #     print(row)


def do_insert():
    new_name = input('Enter an artist name: ')
    sql = """
INSERT INTO artists
(Name)
VALUES
(?)
"""
    print(sql)
    cursor.execute(sql, [new_name])
    conn.commit()
        
if __name__ == '__main__':
    do_insert()