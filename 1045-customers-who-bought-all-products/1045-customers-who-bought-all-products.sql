/*
select customer_id
from customer
group by customer_id
having count(distinct product_key) = (select count(*) from product)
*/
select customer_id
from customer
group by customer_id
having count(distinct product_key) = (select count(*) from product)
    #Prodduct table doesn't need distinct cause it doesn't duplicate