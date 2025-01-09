class Album:
    def __init__(self, title):
        self.title = title

    @property
    def songs(self):
        """Lookup all songs for this album"""
        # print(f'looking up songs for {self}')
        result = []
        for song in Song.all:
            # check if this song belongs to this album
            if song.album is self:  # song.album == myself
                result.append(song)
        return result
    
    def get_total_runtime(self):
        total = 0
        for song in self.songs:
            total += song.runtime
        return total

    def __repr__(self):
        return f'<Album {self.title}>'
    

class Song:
    all = []  # collection of all constructed songs

    def __init__(self, title, runtime, album=None):
        self.title = title
        self.runtime = runtime
        self.album = album
        Song.all.append(self)  # add this song object to Song.all

    def __repr__(self):
        return f'<Song {self.title}, {self.runtime} secs>'


a1 = Album(title='Jagged Little Pill')
s1 = Song(title='You Oughta Know', runtime=120, album=a1)
s2 = Song(title='Hand in my Pocket', runtime=180, album=a1)

a2 = Album(title='Back to Black')
s3 = Song(title='Back to Black', runtime=200, album=a2)
