/*
(
select u.name as results
from users u
inner join movierating mo
    on u.user_id = mo.user_id
group by u.user_id, u.name
order by count(mo.movie_id) desc, u.name asc
limit 1
)
union all
(
select m.title as results
from movies m
inner join movierating mo
    on m.movie_id = mo.movie_id
where mo.created_at between '2020-02-01' and '2020-02-29'
group by mo.movie_id
order by avg(mo.rating) desc, m.title asc
limit 1
)
*/

(
    select u.name as results
    from users u
        join movierating mr
            on u.user_id = mr.user_id
    group by u.user_id, u.name
    order by count(mr.movie_id) desc, u.name asc
    limit 1
)
union all
(
    select mo.title as results
    from movies mo
        join movierating mr
            on mo.movie_id = mr.movie_id
    where mr.created_at between '2020-02-01' and '2020-02-29'
    group by mo.movie_id, mo.title
    order by avg(rating) desc, mo.title asc
    limit 1
)

