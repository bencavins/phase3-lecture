-- CRUD (Create, Read, Update, Delete)
-- (create table and insert into, select, update, delete)

-- get all rows and columns from albums table
SELECT *
FROM albums;

-- get specific columns from albums table
SELECT Title, AlbumId
FROM albums;

-- only return tracks with runtime > 900000
SELECT *
FROM tracks
WHERE Milliseconds > 900000;

-- only return track with id 620
SELECT *
FROM tracks
WHERE TrackId == 620;

-- can use like clause for pattern matching
SELECT *
FROM tracks
WHERE Name LIKE "%the%";

-- limit the result set 
SELECT *
FROM tracks
LIMIT 5;

-- join data from two different tables
SELECT *
FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId;

-- sort data by artist name with order by
SELECT *
FROM artists  -- left table
JOIN albums /* right table */ ON albums.ArtistId == artists.ArtistId 

-- we can go aggregations with group by
SELECT artists.Name, albums.Title, AVG(tracks.Milliseconds)
FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN tracks ON tracks.AlbumId = albums.AlbumId
GROUP BY artists.Name, albums.Title
ORDER BY artists.Name;


-- create a new table 
CREATE TABLE test_table (
	id INTEGER PRIMARY KEY,
	name TEXT,
	age INTEGER,
	fave_color TEXT
);
COMMIT;  -- like hitting "save"


-- insert three rows into the table
INSERT INTO test_table (name, age, fave_color)
VALUES ("alice", 33, "red"), 
("bob", 23, "blue"),
("charlie", 77, "green");

-- delete rows from table
DELETE FROM test_table
WHERE id = 8;

-- update row 3 
UPDATE test_table
SET fave_color = "yellow"
WHERE id = 3;
