# Write your MySQL query statement below
select id, movie, description, rating
from cinema
where id%2 != 0
    and description not like 'boring' #'is not' -> for NULL, 'not like' -> for varchar
order by rating desc