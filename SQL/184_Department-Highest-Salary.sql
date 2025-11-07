SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e, Department d
WHERE e.departmentId = d.id
  AND e.salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = e.departmentId
  );
  
-- Runtime 984 ms
-- Beats 27.57%