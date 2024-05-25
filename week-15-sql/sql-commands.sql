/* Create two tables: bands and albums */
CREATE TABLE bands (
  id SERIAL NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE albums (
  id SERIAL NOT NULL,
  name VARCHAR(255) NOT NULL,
  release_year INT,
  band_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (band_id) REFERENCES bands(id)
);

/* Inserting records to bands and albums tables */
INSERT INTO bands (name)
  VALUES ('Iron  Maiden');

INSERT INTO bands (name)
  VALUES ('Deuce'), ('Avenged Sevenfold'), ('Ankor');

INSERT INTO albums (name, release_year, band_id)
  VALUES ('The Number of the Beasts', 1985, 1),
         ('Power Slave', 1984, 1),
         ('Nightmare', 2018, 2),
         ('Nightmare', 2010, 3),
         ('Test Album', NULL, 3);

/* Querying from bands table */
SELECT * FROM bands;

SELECT * FROM bands LIMIT 2;

SELECT name FROM bands;

SELECT id AS "ID", name AS "Band Name"
  FROM bands;

SELECT * FROM bands ORDER BY name;

SELECT * FROM bands ORDER BY name ASC;

SELECT * FROM bands ORDER BY name DESC;


/* Querying and updating in albums table */
SELECT * FROM albums;

SELECT DISTINCT name FROM albums;

UPDATE albums
  SET release_year = 1982
  WHERE id = 1;
SELECT * FROM albums ORDER BY id;

SELECT * FROM albums
  WHERE release_year < 2000;

SELECT * FROM albums
  WHERE name LIKE '%er' OR band_id = 2;

SELECT * FROM albums
  WHERE release_year = 1984 AND band_id = 1;

SELECT * FROM albums
  WHERE release_year BETWEEN 2000 AND 2018;

SELECT * FROM albums
  WHERE release_year IS NULL;

DELETE FROM albums
  WHERE id = 5;
SELECT * FROM albums;

/* JOIN command */
SELECT * FROM bands
  /*JOIN albums ON bands.id = albums.band_id*/
  JOIN albums ON albums.band_id = bands.id
  ORDER BY albums.id;

SELECT * FROM albums
  JOIN bands ON albums.band_id = bands.id
  ORDER BY albums.id;

/* bands (left) | albums (right) */
SELECT * FROM bands
  LEFT JOIN albums ON bands.id = albums.band_id
  ORDER BY albums.id;

/* Aggregate functions */
SELECT AVG (release_year) FROM albums;

SELECT SUM (release_year) FROM albums;

/* How many occurrences of band_id */ 
SELECT band_id, COUNT (band_id) FROM albums
  GROUP BY band_id
  ORDER BY band_id;

/* Add band name to the above query */
/* bands (left) | albums (right) */
/* COUNT (albums.id) is calculated over
   and aggregated bands.id */
SELECT bands.name, COUNT (albums.id) FROM bands
  LEFT JOIN albums ON bands.id = albums.band_id
  GROUP BY bands.id;

/* Order based on COUNT (albums.id) */
SELECT bands.name AS band_name, COUNT (albums.id) AS num_albums 
  FROM bands
  LEFT JOIN albums ON bands.id = albums.band_id
  GROUP BY bands.id
  ORDER BY num_albums DESC;

/* Select specific num_albums */
/* In PostgreSQL, we cannot use alias in HAVING statement 
   we need to use full aggregation function */
SELECT bands.name AS band_name, COUNT (albums.id) AS num_albums 
  FROM bands
  LEFT JOIN albums ON bands.id = albums.band_id
  GROUP BY bands.id
  HAVING COUNT (albums.id) = 1;

/* With multiple condition in HAVING statement */
SELECT bands.name AS band_name, COUNT (albums.id) AS num_albums 
  FROM bands
  LEFT JOIN albums ON bands.id = albums.band_id
  GROUP BY bands.id
  HAVING COUNT (albums.id) = 1 AND bands.name = 'Deuce';