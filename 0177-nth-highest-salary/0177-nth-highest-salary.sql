CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
/*
BEGIN
  declare M int; #use M to store the offset value
  set M = N-1;
  RETURN (
    select distinct salary
    from employee
    order by salary desc
    limit 1 offset M
  );
END
*/
begin
declare m int;
set m = N-1;
return(
    select distinct salary
    from employee
    order by salary desc
    limit 1 offset m
);
end