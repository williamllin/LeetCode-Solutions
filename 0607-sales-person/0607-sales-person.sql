select sa.name as name
from salesperson sa
where sa.sales_id NOT IN (
    select o.sales_id
    from orders o
        left join company c
            on o.com_id = c.com_id
    where c.name LIKE 'RED'
)
