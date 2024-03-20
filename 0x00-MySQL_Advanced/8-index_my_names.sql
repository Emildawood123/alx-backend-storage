-- create index for names table
CREATE INDEX idx_name_first_score
ON names (name(1));