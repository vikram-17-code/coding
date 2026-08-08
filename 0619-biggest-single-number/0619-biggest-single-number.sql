# Write your MySQL query statement below
SELECT MAX(NUM) as num FROM (select num from MyNumbers group by num having count(*) = 1 )  as a