# Write your MySQL query statement below
select e.email AS Email from Person e Group By email having count(*)>1;