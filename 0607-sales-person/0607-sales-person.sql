/*
select s.name
from salesperson s
where s.sales_id not in (
    select o.sales_id
    from orders o
    join company c
        on o.com_id = c.com_id
    where c.name ='RED'
)
#where xxx IN/NOT IN, if where xxx is one column, the subquery should be one column as well

*/
select s.name as name
from salesperson s
where s.sales_id not in (
    select o.sales_id
    from orders o
    join company c
        on o.com_id = c.com_id
    where c.name like 'RED'
)













