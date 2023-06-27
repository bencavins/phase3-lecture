import sqlite3

conn = sqlite3.connect('book.db')
cursor = conn.cursor()

class Book:
    def __init__(self, title, author):
        self.id = None
        self.title = title
        self.author = author
    
    @classmethod
    def create_table(cls):
        sql = '''CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT
        )
        '''
        cursor.execute(sql)
    
    @classmethod
    def drop_table(cls):
        sql = '''DROP TABLE books'''
        cursor.execute(sql)
    
    def save(self):
        """Save a *new* the book instance to the db"""
        sql = '''INSERT INTO books
        (title, author)
        VALUES
        (?, ?)
        '''
        cursor.execute(sql, (self.title, self.author))
    
    def update(self):
        sql = '''UPDATE books
        SET title = ?, author = ?
        WHERE id = ?
        '''
        cursor.execute(sql, (self.title, self.author, self.id))
    
    @classmethod
    def get_by_id(cls, id):
        sql = '''SELECT title, author, id
        FROM books
        WHERE id = ?
        '''
        result = cursor.execute(sql, (id,)).fetchone()
        book = Book(title=result[0], author=result[1])
        book.id = result[2]
        return book

    
    def __repr__(self) -> str:
        return f"<Book {self.title} by {self.author}>"