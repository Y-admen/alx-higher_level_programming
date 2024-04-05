-- Returns the name and highest score records from the second_table table, 
-- ordered by score descending. This gets the top scoring records.
SELECT score, name 
FROM second_table 
WHERE score >= 10
ORDER BY score DESC;
