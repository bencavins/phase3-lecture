class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


if __name__ == '__main__':
    # create some artist/albums
    my_artist = Artist('Avril Lavigne')
    album = Album('Let Go', my_artist)
    another_album = Album('Love Sucks', my_artist)

    # link the artist to the album
    # album.artist = my_artist

    # link the albums to the artist
    my_artist.albums.append(album)
    my_artist.albums.append(another_album)

    
    for album in my_artist.albums:
        print(album.title)