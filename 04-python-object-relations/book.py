"""
1 User -> * Reviews
1 Book -> * Reviews
1 Reivew -> 1 Book, 1 User
"""

class Book:
    def __init__(self, title):
        self.title = title
        self.reviews = []
    
    def get_all_users(self):
        return [r.user for r in self.reviews]

    def get_avg_rating(self):
        return sum([r.rating for r in self.reviews]) / len(self.reviews)
    
    def __repr__(self) -> str:
        return f"<Book {self.title}>"

if __name__ == '__main__':
    from user import User
    from review import Review

    b1 = Book('Catch-22')
    b2 = Book('3 Musketeers')

    u1 = User('joe')
    u2 = User('bono')

    r1 = Review(b1, u1, 5)
    r2 = Review(b1, u2, 3)
    r3 = Review(b2, u2, 4)
