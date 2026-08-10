/*
with rankedemployee as (
    select salary,
    dense_rank()over(order by salary desc) as salary_rank
    #rank through salary and create column:salary_rank
    from employee
)
select max(salary) as SecondHighestSalary
from rankedemployee
where salary_rank = 2
*/





with rankedsalary as(
    select id, salary,
        dense_rank()over(order by salary desc) as salary_ranked
    from employee
)
#use max() so that if no 2ng high, return NULL
#since agg: if nothing and no group by, will return null
select max(salary) as SecondHighestSalary 
from rankedsalary
where salary_ranked = 2
