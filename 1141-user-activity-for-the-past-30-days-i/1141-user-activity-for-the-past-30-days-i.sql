# Write your MySQL query statement below
select activity_date as day, count(distinct user_id) as active_users
from activity
where activity_date BETWEEN '2019-06-28' AND '2019-07-27'
#WHERE DATEDIFF('2019-07-27', activity_date) >= 0  to prevent ex:2019/8/1 -> -5<=30 
  #AND DATEDIFF('2019-07-27', activity_date) < 30
group by day