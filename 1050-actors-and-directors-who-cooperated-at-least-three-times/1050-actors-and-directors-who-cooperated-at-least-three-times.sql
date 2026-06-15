# Write your MySQL query statement below
select actor_id, director_id
from actordirector
where (actor_id, director_id) in (
    select actor_id, director_id
    from actordirector
    group by actor_id, director_id
    having count(*) >= 3
)
group by actor_id, director_id