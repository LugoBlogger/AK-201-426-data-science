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
  FOREIGN KEY (band_id) REFERENCES bands (id)
);

INSERT INTO bands (name)
  VALUES ('Iron Maiden');

INSERT INTO bands (name)
  VALUES ('Deuce'), ('Avenged Sevenfold'), ('Ankor');

INSERT INTO albums (name, release_year, band_id)
  VALUES ('The Number of the Beasts', 1985, 1),
         ('Power Slave', 1984, 1),
         ('Nightmare', 2018, 2), 
         ('Nightmare', 2010, 3),
         ('Test Album', NULL, 3);

SELECT * FROM bands;

SELECT * FROM bands LIMIT 2;

SELECT name FROM bands;

SELECT id AS "ID", name AS "Band Name"
  FROM bands;

SELECT name FROM bands ORDER BY name;

SELECT * FROM albums;

/* Take distinct elements */
SELECT DISTINCT name FROM albums;

UPDATE albums
  SET release_year = 1982
  WHERE id = 1;
SELECT * FROM albums ORDER BY id;

SELECT * FROM albums
  WHERE release_year < 2000;

SELECT * FROM albums
  WHERE name LIKE '%Pow%';

SELECT * FROM albums
  WHERE release_year IS NULL;

DELETE FROM albums
  WHERE id = 5;
SELECT * FROM albums;

SELECT * FROM bands
  JOIN albums ON bands.id = albums.band_id;

SELECT * FROM albums
  JOIN bands ON bands.id = albums.band_id;