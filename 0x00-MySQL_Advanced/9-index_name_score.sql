-- This index is created using the CREATE INDEX statement
-- with the index name idx_name_first_score
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);
