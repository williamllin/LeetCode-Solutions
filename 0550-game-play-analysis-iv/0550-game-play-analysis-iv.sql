/*
select round(count(a2.player_id)/count(a1.player_id),2) as fraction
from (
    select player_id, min(event_date) as first_login
    from activity
    group by player_id
) a1 left join activity a2
        on a1.player_id = a2.player_id
        and datediff(a2.event_date, a1.first_login) = 1
#分母:所有人的第一次登入(a1)
#分子:跟第一次登入差一天的才算(a2)
*/

select round(count(a1.player_id)/count(a2.player_id),2) as fraction
from activity a1
    right join (
        select player_id, min(event_date) as first_login
        from activity
        group by player_id 
    ) a2 on a1.player_id = a2.player_id
            and datediff(a1.event_date, a2.first_login) = 1











