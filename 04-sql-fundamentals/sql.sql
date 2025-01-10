-- Select all from table
SELECT *
FROM artists;

-- Select specific columns from table
SELECT InvoiceDate, Total
FROM invoices;

-- Can filter out rows with WHERE
SELECT *
FROM invoices
WHERE Total > 10;

-- Can have multiple WHERE conditions (AND/OR)
SELECT * 
FROM invoices 
WHERE Total > 10 
	AND BillingCity == "Boston";

-- Can pattern match
SELECT * 
FROM artists
WHERE Name LIKE "B%";  -- Name starts with B

-- Join two tables together
SELECT *
FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId;

-- Order by a column (can add DESC)
SELECT *
FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
ORDER BY ArtistId; -- DESC

-- More complicated JOIN (multiple tables)
SELECT tracks.Name, albums.Title,  artists.Name
FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN tracks ON tracks.AlbumId = albums.AlbumId
ORDER BY artists.Name, albums.Title;



-- CREATE a new table
CREATE TABLE IF NOT EXISTS person (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	age INTEGER,
	hobby TEXT DEFAULT "unknown"
)

-- INSERT into a table
INSERT INTO person
(name, age, hobby)
VALUES
("Alice", 23, "basketball"),
("Bob", 55, "movies"),
("Charlie", 12, "video games")

-- UPDATE data
UPDATE person
SET hobby = "coding", age = 99
WHERE id = 4

-- DELETE rows
DELETE FROM person
WHERE id = 6

-- Delete a table
DROP TABLE person