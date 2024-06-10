-- CRUD (Create, Read, Update, Delete)

-- select all rows and cols from one table
SELECT *
FROM artists

-- filter data with WHERE clause
SELECT *
FROM artists
WHERE ArtistId > 100 AND ArtistId < 110

-- filter data with WHERE clause and like
SELECT *
FROM artists
WHERE Name like "Mot%"

-- can limit number of rows with LIMIT
SELECT *
FROM artists
LIMIT 4

-- can join tables together with JOIN
SELECT *
FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
ORDER BY artists.Name

-- can use multiple joins for many-to-many relationships
SELECT *
FROM playlists
JOIN playlist_track on playlist_track.PlaylistId = playlists.PlaylistId
JOIN tracks on tracks.TrackId = playlist_track.TrackId
WHERE tracks.TrackId = 1

-- create a new table
CREATE TABLE test_table (
	id INTEGER PRIMARY KEY,
	name TEXT,
	age INTEGER,
	float NUMERIC
)

-- bulk insert data into TABLE
INSERT INTO test_table (age, float, name)
VALUES (90, 4.44, "bob"),
(45, 1.2, "anne"),
(6, 9, "Zed")

-- update existing data
UPDATE test_table 
SET name = "Paul", age = 99
WHERE id = 1

-- add column to table
ALTER TABLE test_table 
ADD COLUMN new_col TEXT;

-- delete rows from table
DELETE FROM test_table
WHERE id = 2

-- delete whole table
DROP TABLE test_table