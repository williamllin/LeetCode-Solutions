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


/*
table after join:
e.id   e.name   e.dep   e.magId   ma.name   ma.id
102    dan      a       101       john      101
103    james    a       101       john      101
104    amy      a       101       john      101
105    anne     a       101       john      101
106    ron      b       101       john      101
*/