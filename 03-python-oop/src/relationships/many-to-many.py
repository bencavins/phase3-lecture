class Movie:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if len(new_title) > 0:
            self._title = new_title
        else:
            raise ValueError('invalid title')

    def get_showtimes(self):
        """Filter through ShowTime.all to get only showtimes for this movie"""
        result = []
        for showtime in ShowTime.all:
            if showtime.movie is self:
                result.append(showtime)
        return result
    
    def get_theaters(self):
        theaters = set()
        for showtime in self.get_showtimes():
            theaters.add(showtime.theater)
        return theaters

    def __repr__(self) -> str:
        return f'<Movie {self.title}>'


class ShowTime:
    all = []

    def __init__(self, time, movie, theater):
        self.time = time
        self.movie = movie  # will be a Movie object
        self.theater = theater  # will be a Theater object

        ShowTime.all.append(self)  # add showtime to array of all showtimes
    
    def __repr__(self) -> str:
        return f'<Showtime {self.movie.title} {self.time}>'


class Theater:
    def __init__(self, name):
        self.name = name

    def get_showtimes(self):
        """Filter through ShowTime.all to get only showtimes for this theater"""
        result = []
        for showtime in ShowTime.all:
            if showtime.theater is self:
                result.append(showtime)
        return result
    
    def get_movies(self):
        movies = set()
        for showtime in self.get_showtimes():  # this does the filtering 
            movies.add(showtime.movie)
        return movies
    
    def __repr__(self) -> str:
        return f'<Theater {self.name}>'
    


m1 = Movie('avatar')
m2 = Movie('LEGO')

t1 = Theater('amc')
t2 = Theater('alamo')

s1 = ShowTime(1200, m1, t1)
s1 = ShowTime(1300, m1, t1)
s1 = ShowTime(1400, m1, t1)
s2 = ShowTime(100, m1, t2)
s3 = ShowTime(300, m2, t1)
