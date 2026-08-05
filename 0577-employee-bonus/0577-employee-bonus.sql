# Write your MySQL query statement below
select E.name, B.bonus from Employee E left join Bonus B on e.empID=b.empID where B.bonus <1000 or B.bonus is Null;