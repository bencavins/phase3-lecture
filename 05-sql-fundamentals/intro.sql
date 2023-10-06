-- SQLite
-- get all rows and columns from albums
SELECT *
FROM albums

-- get all rows and columns from albums
SELECT Title, AlbumId
FROM albums

-- can filter data with WHERE
SELECT *
FROM albums
WHERE AlbumId > 10 AND AlbumId < 20

-- Can sort with ORDER BY
SELECT *
FROM albums
WHERE AlbumId > 10 AND AlbumId < 20
ORDER BY Title

-- query data from multiple tables with JOIN
SELECT artists.Name, albums.Title
FROM albums
JOIN artists
  ON albums.ArtistId == artists.ArtistId
ORDER BY artists.Name


-- create a table
CREATE TABLE my_table (
  cola INTEGER,
  colb DECIMAL,
  colc TEXT
)

-- insert data
INSERT INTO my_table
(cola, colb, colc)  -- the column names
VALUES
(1, 3.14, "hello"),  -- the actual data to insert
(2, 9.99, "world")