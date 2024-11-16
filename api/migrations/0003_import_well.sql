INSERT INTO wells(well, ngdu, cdng, kust, mest)
    SELECT
        id,
        id / 1000,
        id / 100,
        id / 10,
        (
        CASE
            WHEN id / 100 IN (14, 35, 21, 42) THEN -1
            WHEN id / 100 IN (15, 22, 43) THEN -2
            WHEN id / 100 IN (16, 23, 44) THEN -3
            WHEN id / 100 IN (17, 31, 24) THEN -4
            WHEN id / 100 IN (11, 32, 25) THEN -5
            WHEN id / 100 IN (12, 33, 26) THEN -6
            WHEN id / 100 IN (13, 34, 41) THEN -7
        END
        )
    FROM objects WHERE type = 4
ON CONFLICT (well)
DO UPDATE SET
    ngdu = EXCLUDED.ngdu,
    cdng = EXCLUDED.cdng,
    kust = EXCLUDED.kust,
    mest = EXCLUDED.mest;