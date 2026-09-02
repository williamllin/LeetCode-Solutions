/*
select e.name as name
from employee e
where e.id in (
    select managerId
    from employee
    group by managerId
    having count(id)>=5
)
*/
select ma.name
from employee e
    join (
        select id, name
        from employee e
    ) ma 
        on e.managerId = ma.id
group by ma.id, ma.name
having count(e.id)>=5
