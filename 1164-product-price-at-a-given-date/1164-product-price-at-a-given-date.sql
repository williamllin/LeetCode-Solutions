# Write your MySQL query statement below

#prices changed before or on 2019-08-16
select product_id, new_price as price
from products
where(product_id, change_date) in (
    select product_id, max(change_date)
    from products
    where change_date <='2019-08-16'
    group by product_id
)

union

#prices after 2019-08-16
select product_id, 10 as price
from products
group by product_id
having min(change_date) >'2019-08-16'