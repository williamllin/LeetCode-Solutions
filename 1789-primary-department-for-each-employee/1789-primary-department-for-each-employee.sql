/*
select employee_id, department_id
from employee

where primary_flag = 'Y'
    or employee_id in (
        select employee_id
        from employee
        group by employee_id
        having count(department_id)=1
    )
*/
select employee_id, department_id
from employee
where primary_flag like 'Y'
    or employee_id in(
        select employee_id
        from employee
        group by employee_id
        having count(primary_flag)=1
    )
#"LIKE" operator is used for string pattern matching with wildcards
#"IS" operator is used specifically to evaluate NULL states