CREATE INDEX idx_wells_ngdu ON wells(ngdu);
CREATE INDEX idx_wells_cdng ON wells(cdng);
CREATE INDEX idx_wells_kust ON wells(kust);
CREATE INDEX idx_wells_mest ON wells(mest);

CREATE INDEX idx_well_day_histories_date_well ON well_day_histories(date_add, well);

CREATE INDEX idx_objects_type_name ON objects(type, name);
CREATE INDEX idx_objects_name ON objects(name);

CREATE INDEX idx_objects_coordinates_id ON objects_coordinates(id);
CREATE INDEX idx_well_day_plans_date_well ON well_day_plans(date_add, well);
