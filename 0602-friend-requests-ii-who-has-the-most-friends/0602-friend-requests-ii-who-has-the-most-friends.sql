#when appear in either requester or accepter, count as a num, since no 'a to b' and 'b accept a' situation 
with allfriend as (
    select requester_id as id from requestaccepted
    union all #use union all so that NO 'distinct' function
    select accepter_id as id from requestaccepted
)
#make requester, accepter columns into the same column and count it.

select id, count(*) as num
from allfriend
group by id
order by num desc
limit 1