# Write your MySQL query statement below
select E.name AS Employee from Employee E join Employee M on E.managerId = M.id where E.salary > M.salary;