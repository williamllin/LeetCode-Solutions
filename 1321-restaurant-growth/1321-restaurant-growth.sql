/*
with dailyamount as ( #since some rows are same date
    select visited_on, sum(amount) as daily_amount
    from customer
    group by visited_on
),

movingmetrics as (
    select 
        visited_on,
        sum(daily_amount)over(order by visited_on rows 6 preceding) as amount, #sum every 6 days
        round(avg(daily_amount)over(order by visited_on rows 6 preceding),2) as average_amount #avg every 6days
    from dailyamount
)
select visited_on, amount, average_amount
from movingmetrics
where datediff(visited_on, (select min(visited_on) from movingmetrics)) >=6
order by visited_on asc
*/

#amount per day(since multiple entry with same date)
with dailyamount as(
    select visited_on, sum(amount) as dailyamount
    from customer
    group by visited_on
),

#moving metrics
movingmetrics as(
    select visited_on, 
        sum(dailyamount)over(order by visited_on rows 6 preceding) as amount,
        round(avg(dailyamount)over(order by visited_on rows 6 preceding),2) as average_amount
    from dailyamount
)

#output
select visited_on, amount, average_amount
from movingmetrics
where datediff(visited_on, (select min(visited_on) from movingmetrics)) >=6
order by visited_on asc















