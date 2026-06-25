select p.project_id, round(avg(e.experience_years),2) as average_years
from project p
    left join employee e
        on p.employee_id = e.employee_id
group by p.project_id

/*
**project id   emp id        emp id        name     **exp.years
| 1           | 1           | 1           | Khaled | 3                |
| 1           | 2           | 2           | Ali    | 2                |
| 1           | 3           | 3           | John   | 1                |
| 2           | 1           | 1           | Khaled | 3                |
| 2           | 4           | 4           | Doe    | 2                |
*/