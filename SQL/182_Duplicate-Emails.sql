SELECT email AS Email FROM Person
GROUP BY email
HAVING COUNT(email) > 1;

-- Runtime 376 ms
-- Beats 35.24%