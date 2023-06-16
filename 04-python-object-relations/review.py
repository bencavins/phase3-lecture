class Review:
    def __init__(self, book, user, rating):
        self.user = user
        self.book = book
        self.rating = rating
        self.user.reviews.append(self)
        self.book.reviews.append(self)
    
    def __repr__(self) -> str:
        return f"<Review {self.user} {self.book} {self.rating}>"