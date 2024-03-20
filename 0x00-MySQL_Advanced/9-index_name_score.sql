-- create index and add 2
CREATE INDEX idx_name_first_score
ON names (name(1), score);
