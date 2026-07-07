/*
select(
    select distinct salary
    from employee
    order by salary desc
    limit 1 offset 1
) as SecondHighestSalary
*/

with rankedemployee as (
    select salary
    ,dense_rank() over(order by salary desc) as salary_rank 
    #rank through salary and create column:salary_rank
    from employee
)
select max(salary) as SecondHighestSalary
from rankedemployee
where salary_rank = 2
