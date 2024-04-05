-- This query selects the score and count of scores from the second_table table, 
-- groups the results by score, orders them descending by score, 
-- and aliases the count of scores column as 'number'.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
