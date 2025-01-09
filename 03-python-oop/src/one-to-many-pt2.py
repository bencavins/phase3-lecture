class Artist:
    def __init__(self, name):
        self.name = name

    @property
    def albums(self):
        result = []
        for album in Album.all:
            if album.artist is self:
                result.append(album)
        return result
    
    def get_all_songs(self):
        all_songs = []
        for album in self.albums:
            for song in album.songs:
                all_songs.append(song)
        return all_songs

    def __repr__(self):
        return f'<Artist: {self.name}>'


class Album:
    all = []

    def __init__(self, title, artist=None):
        self.title = title
        self.artist = artist
        Album.all.append(self)

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
        return f'<Album: {self.title}>'
    

class Song:
    all = []  # collection of all constructed songs

    def __init__(self, title, runtime, album=None):
        self.title = title
        self.runtime = runtime
        self.album = album
        Song.all.append(self)  # add this song object to Song.all

    def __repr__(self):
        return f'<Song: {self.title}, {self.runtime} secs>'


art1 = Artist(name='Alanis Morrisette')

a1 = Album(title='Jagged Little Pill', artist=art1)
s1 = Song(title='You Oughta Know', runtime=120, album=a1)
s2 = Song(title='Hand in my Pocket', runtime=180, album=a1)

a3 = Album(title='test', artist=art1)
s4 = Song(title='songa', runtime=120, album=a3)
s5 = Song(title='songb', runtime=180, album=a3)

art2 = Artist(name='Amy Winehouse')
a2 = Album(title='Back to Black', artist=art2)
s3 = Song(title='Back to Black', runtime=200, album=a2)
