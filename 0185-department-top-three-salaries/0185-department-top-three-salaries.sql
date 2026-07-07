with rankedsalary as (
    select
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        dense_rank()over(
            partition by e.departmentId #within each department(partition by)
            order by e.salary desc          #rank salary(order by)
        ) as salary_rank 
    from employee e
        inner join department d
        on e.departmentId = d.id
)

select Department, Employee, Salary
from rankedsalary
where salary_rank <=3
