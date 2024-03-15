class User:
    def __init__(self, username):
        self.username = username

    def get_reviews(self):
        # loop through all reviews, find the ones written by this user
        result = []
        for review in Review.all:
            if review.user is self:
                result.append(review)
        return result
    
    def get_movies(self):
        result = []
        reviews = self.get_reviews()
        for review in reviews:
            result.append(review.movie)
        return result
        # return [review.movie for review in self.get_reviews()]

    def __repr__(self):
        return f"<User {self.username}>"


class Review:
    all = []

    def __init__(self, rating, user, movie):
        self.rating = rating
        self.user = user
        self.movie = movie
        Review.all.append(self)

    def __repr__(self):
        return f"<Review {self.rating} {self.user.username} {self.movie.title}>"


class Movie:
    def __init__(self, title):
        self.title = title

    def get_reviews(self):
        result = []
        for review in Review.all:
            if review.movie is self:
                result.append(review)
        return result
    
    def __repr__(self):
        return f"<Movie {self.title}>"
    


joe = User('joe123')
# joe is an obj
# joe.username is a string 'joe123'
anne = User('anne789')

joe.get_reviews()
anne.get_reviews()

m1 = Movie('shawsank redemption')
m2 = Movie('finding nemo')
m3 = Movie('shrek')

Review(10, joe, m1)
Review(9, joe, m2)
Review(8, anne, m3)