with damount as(
    select visited_on, sum(amount) as dailyamount
    from customer
    group by visited_on
),

movingmetrics as (
    select visited_on,
    sum(dailyamount)over(order by visited_on rows 6 preceding) as amount,
    round(avg(dailyamount)over(order by visited_on rows 6 preceding),2) as average_amount,
    row_number()over(order by visited_on) as rn
    from damount
)

select visited_on, amount, average_amount
from movingmetrics 
where rn>=7
order by visited_on asc