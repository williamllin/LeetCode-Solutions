with ranked_salary as(
    select d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        dense_rank()over(partition by e.departmentId order by e.salary desc) as rank_sal
    from employee e
        join department d
            on e.departmentId = d.id
)
select Department, Employee, Salary
from ranked_salary
where rank_sal = 1