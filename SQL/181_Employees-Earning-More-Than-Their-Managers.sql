SELECT e.name as Employee
FROM Employee e
JOIN Employee m 
On e.managerId = m.id
where e.salary > m.salary;

-- Runtime 362 ms
-- Beats 56.30%
