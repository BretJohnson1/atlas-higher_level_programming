-- This script lists all records of a specific table
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC, name DESC;
