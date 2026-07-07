



with allfriend as(
    select requester_id as id from requestaccepted
    union all
    select accepter_id as id from requestaccepted
)

select id, count(*) as num
from allfriend
group by id
order by num desc
limit 1














