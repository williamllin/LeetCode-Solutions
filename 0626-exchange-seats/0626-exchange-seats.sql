/*
SELECT 
    id,
    CASE 
        #COALESCE: if next line is NULL, keep it's own name
        #odd: use LEAD to grab next one
        WHEN id % 2 = 1 THEN COALESCE(LEAD(student, 1) OVER(ORDER BY id), student)
        #even: use LAG to grab previous one
        ELSE LAG(student, 1) OVER(ORDER BY id)
    END AS student
FROM seat
*/


/*
lag: take previous
lead: take next
coalesce: if NULL, use original(ex: no id6, so use Jeames)
*/

select id, 
    case
        when id%2=1 then coalesce(lead(student,1) over(order by id), student)
        else lag(student,1) over(order by id)
    end as student
from seat


