select e1.employee_id, e1.name
        , count(e2.reports_to) as reports_count, round(avg(e2.age)) as average_age
from employees e1
    inner join employees e2 
        on e1.employee_id = e2.reports_to 
group by e1.employee_id, e1.name
order by e1.employee_id

/*
e1.emp_id   e1.name   e1.age | e2.emp_id  e2.name   e2.reports_to  e2.age
9           hercy     43       6          alice     9              41
9           hercy     43       4          bob       9              36
6           alice     41       6          alice (this row won't exist)
4           bob       36       4          bob (this row won't exist)     
2           winston   37       2          winston (this row won't exist)
*/
