CREATE TABLE IF NOT EXISTS objects_coordinates(  
    id integer PRIMARY KEY REFERENCES objects(id),
    lat FLOAT,
    lon FLOAT
);

INSERT INTO objects_coordinates (id, lat, lon)
    SELECT 
        id, 
        60 + (RANDOM() * (65 - 60)),
        60 + (RANDOM() * (75 - 60))
    FROM objects
    WHERE type = 4;
