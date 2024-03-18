-- Select all rows from artists
SELECT Name, ArtistId
FROM artists;

-- Filter out some rows
SELECT *
FROM invoices
WHERE total == 13.86 AND BillingCity == "Boston";

-- join two or more tables
SELECT artists.Name, albums.Title, tracks.Name
FROM albums
JOIN artists ON albums.ArtistId = artists.ArtistId
JOIN tracks ON tracks.AlbumId = albums.AlbumId

-- create new table
CREATE TABLE my_table (
	id INTEGER PRIMARY KEY,
	name TEXT,
	value NUMERIC
)

-- delete table
DROP TABLE my_table

-- insert rows
INSERT INTO my_table (name, value)
VALUES 
("some name", NULL),
("another name", 3.14)

-- add new column to existing table
ALTER TABLE my_table
ADD new_column2 INTEGER
DEFAULT 999

-- delete rows
DELETE FROM my_table
WHERE id = 1

-- update data
UPDATE my_table
SET value = 6.28, name = "abc"
WHERE id = 6;