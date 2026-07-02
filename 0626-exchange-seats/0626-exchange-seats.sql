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
