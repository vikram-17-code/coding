CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N-1;
    RETURN (
        select salary from(select distinct salary from Employee order by salary desc) As temp limit 1 OFFSET N
         
    );
END