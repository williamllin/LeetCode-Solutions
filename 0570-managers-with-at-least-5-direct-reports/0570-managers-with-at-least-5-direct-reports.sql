# Write your MySQL query statement below



select ma.name
from employee e
    join (select id, name
          from employee) ma 
            on ma.id = e.managerId
group by ma.id, ma.name
having count(e.id) >=5








