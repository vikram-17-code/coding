# Write your MySQL query statement below
select 
    d.name as Department,
    e.name as Employee,
    e.salary As Salary 
from Employee e 
join Department d 
    on e.departmentId=d.id 
where (e.departmentid,e.salary) in 
    (select departmentid, max(salary) 
    from Employee 
    group by departmentId);