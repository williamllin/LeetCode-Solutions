# Write your MySQL query statement below

/*
SELECT name 
FROM Employee 
WHERE id IN (
    SELECT managerId 
    FROM Employee 
    GROUP BY managerId 
    HAVING COUNT(id) >= 5
)
*/

select ma.name
from employee e
    join (select id, name #inner join to void manager id that doesn't exist in this company(ex:100)
        from employee e) ma
            on e.managerId = ma.id
group by ma.name, ma.id #group by name since name is the main, group by id since people might have same name
having count(e.id) >=5 
#use employee id to count instead manager id, avoid null employee id(some managers might not have employees to match)

/*
table after join:
e.id   e.name   e.dep   e.magId   ma.name   ma.id
102    dan      a       101       john      101
103    james    a       101       john      101
104    amy      a       101       john      101
105    anne     a       101       john      101
106    ron      b       101       john      101
*/


 













