-- index is created using the CREATE INDEX statement
-- with the index name idx_name_first.
CREATE INDEX idx_name_first ON names (LEFT(name, 1));
