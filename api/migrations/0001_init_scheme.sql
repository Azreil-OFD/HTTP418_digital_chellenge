CREATE TABLE IF NOT EXISTS objects_type (
    id bigint PRIMARY KEY,
    name varchar(42)
);

INSERT INTO objects_type (id, name)
VALUES
    (1, 'Месторождение'),
    (2, 'ЦДНГ'),
    (3, 'Куст'),
    (4, 'Cкважина'),
    (5, 'НГДУ')
;

CREATE TABLE IF NOT EXISTS objects (
    id integer PRIMARY KEY,
    name varchar(42),
    type integer references objects_type(id)
);

CREATE TABLE IF NOT EXISTS wells (
    well integer PRIMARY KEY REFERENCES objects(id), -- скважина(«Ресурсный источник»)
    ngdu integer REFERENCES objects(id), -- НГДУ (нефтегазодобывающее управление)
    cdng integer REFERENCES objects(id), -- ЦДНГ (цех добычи нефти и газа)
    kust integer REFERENCES objects(id), -- Куст (кустовая площадка)
    mest integer REFERENCES objects(id) -- Месторождение
);

CREATE TABLE IF NOT EXISTS well_day_histories (
    well integer REFERENCES wells(well),
    date_fact date, -- дата значения
    debit float, -- суточный дебит жидкости в м3
    ee_consume float, -- суточное электропотребление в КВт*ч
    expenses float, -- суточные затраты на содержание в у.е.
    pump_operating float, -- суточная наработка насоса в у.е.

    PRIMARY KEY (well, date_fact)
);

CREATE TABLE IF NOT EXISTS well_day_plans (
    well integer REFERENCES wells(well),
    date_plan date, -- дата значения
    debit float, -- суточный дебит жидкости в м3
    ee_consume float, -- суточное электропотребление в КВт*ч
    expenses float, -- суточные затраты на содержание в у.е.
    pump_operating float, -- суточная наработка насоса в у.е.

    PRIMARY KEY (well, date_plan)
);
