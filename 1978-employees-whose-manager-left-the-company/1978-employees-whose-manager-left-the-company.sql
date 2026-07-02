# Write your MySQL query statement below
#salary<30000, manager_id not in employee_id
select employee_id
from employees
where salary<30000
    and manager_id not in (
        select employee_id
        from employees
    )
order by employee_id asc













