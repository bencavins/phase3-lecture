class User:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def print_all_reviews(self):
        for review in self.reviews:
            print(review)
    
    def print_all_books(self):
        for review in self.reviews:
            print(review.book.title)

class Book:
    def __init__(self, title):
        self.title = title
        self.reviews = []
    
    def print_all_reviews(self):
        for review in self.reviews:
            print(review)
    
    def print_all_users(self):
        for review in self.reviews:
            print(review.user.name)

class Review:
    def __init__(self, user, book, rating):
        self.user = user
        user.reviews.append(self)
        self.book = book
        book.reviews.append(self)
        self.rating = rating
    
    def __repr__(self) -> str:
        return f"<Review user={self.user.name}, book={self.book.title}, rating={self.rating}>"


user = User('joe')
book = Book('Lord of the Rings')
hobbit = Book('The Hobbit')

Review(user, book, 5)
Review(user, hobbit, 4)

hobbit.print_all_users()