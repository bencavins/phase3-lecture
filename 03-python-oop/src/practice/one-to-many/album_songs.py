"""
Create two classes, Album and Song

One album has many songs, one song belongs to one album

Song
- should have an attribute 'title'
- should have an attribute 'runtime'
    - this should be an integer that represents the runtime in seconds
    - write a getter and setter for runtime
    - validate the it is not negative
- should have an attribute 'album' that is a School object

Album
- should have an attribute 'name'
    - write a getter and setter for name
    - validate that name is not empty
- should have an attribute 'artist'
- should have a function get_songs()
    - returns a list of all song objects for that
- should have a function get_total_runtime()
    - returns the sum of all the song runtimes on the album
- should have a function get_shortest_song()
    - returns the song object with the shortest runtime
"""

class Album:
    pass

class Song:
    pass
