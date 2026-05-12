# Write your MySQL query statement below
select ma.name
from employee e
    join (select id, name #inner join to void manager id that doesn't exist in this company(ex:100)
        from employee e) ma
            on e.managerId = ma.id
group by ma.id, ma.name
having count(e.id) >=5 
#use employee id to count instead manager id, avoid null employee id(some managers might not have employees to match)

