select 
    round(avg(case when order_date = customer_pref_delivery_date then 1 else 0 end) * 100, 2) as immediate_percentage 
#this still counts the non-first date, so need subQ to select each customer first date

from delivery
where (customer_id, order_date) in ( 
    select customer_id, min(order_date)
    from delivery
    group by customer_id
)
