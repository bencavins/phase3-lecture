class Theater:
    def __init__(self, name):
        self.name = name

    def get_showtimes(self):
        """Returns all the showtimes for this theater"""
        result = []
        for showtime in ShowTime.all:
            if showtime.theater is self:
                result.append(showtime)
        return result
        # can also do this with list comprehension
        # return [showtime for showtime in ShowTime.all if showtime.theater is self]

    def get_movies(self):
        """Returns all the movies playing at this theater"""
        result = []
        for showtime in self.get_showtimes():  # get_showtimes filters out other theaters for us
            result.append(showtime.movie)  # just append the movie object
        return list(set(result))  # set() de-duplicates the movies (turing back into list is optional)

    def get_highest_grossing_movie(self):
        """Returns the highest grossing movie at this theater"""
        max_movie = self.get_movies()[0]
        for movie in self.get_movies():
            if movie.box_office_gross > max_movie.box_office_gross:
                max_movie = movie
        return max_movie
        # can also do this with max() and lamdba key
        # return max(self.get_movies(), key=lambda movie: movie.box_office_gross)
    
    def get_total_gross(self):
        """Returns the total gross for all movies playing at this theater"""
        pass

    def get_avg_gross(self):
        """Returns the average gross for all movies playing at this theater"""
        pass

    def __repr__(self):
        return f'<Theater {self.name}>'

class Movie:
    def __init__(self, title, box_office_gross=0):
        self.title = title
        self.box_office_gross = box_office_gross

    def get_showtimes(self):
        """Returns all the showtimes for this movie"""
        result = []
        for showtime in ShowTime.all:
            if showtime.movie is self:
                result.append(showtime)
        return result

    def get_theaters(self):
        """Returns all the theaters playing this movie"""
        result = []
        for showtime in self.get_showtimes():
            result.append(showtime.theater)
        return list(set(result))

    def __repr__(self):
        return f'<Movie {self.title}>'

class ShowTime:
    all = []

    def __init__(self, time, movie, theater):
        self.time = time
        self.movie = movie
        self.theater = theater
        ShowTime.all.append(self)
    
    def __repr__(self):
        return f'<ShowTime {self.time} {self.movie.title} {self.theater.name}>'
    

m1 = Movie('The Shining', box_office_gross=150000000)
m2 = Movie('The Life Aquatic', box_office_gross=350000000)

t1 = Theater('AMC')
t2 = Theater('Alamo Drafthouse')

s1 = ShowTime('6:00pm', m1, t1)
s2 = ShowTime('8:00pm', m1, t1)
s3 = ShowTime('6:00pm', m1, t2)
s4 = ShowTime('12:00pm', m2, t1)

print(t1.get_highest_grossing_movie())