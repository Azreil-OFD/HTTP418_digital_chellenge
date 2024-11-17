CREATE TABLE IF NOT EXISTS objects_coordinates(  
    id integer PRIMARY KEY REFERENCES objects(id),
    lat FLOAT,
    lon FLOAT
);

INSERT INTO objects_coordinates (id, lat, lon)
SELECT
    id,
    55 + (RANDOM() * (67 - 55)),
    60 + (RANDOM() * (80 - 60))
FROM objects
WHERE type = 3;
