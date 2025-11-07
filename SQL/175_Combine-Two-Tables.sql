-- # Write your MySQL query statement below
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person LEFT JOIN Address ON Person.personId=address.personId;

-- Update address 
-- set addressId = NULL
-- where 

-- Runtime 252 ms
-- Beats 70.97%
