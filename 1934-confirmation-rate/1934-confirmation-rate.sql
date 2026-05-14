# Write your MySQL query statement below
select s.user_id, 
round(
    avg(IF(c.action = 'confirmed', 1, 0)) #if confirmed -> 1, otherwise 0
,2) as confirmation_rate

from signups s 
    left join confirmations c 
        on s.user_id = c.user_id
group by s.user_id