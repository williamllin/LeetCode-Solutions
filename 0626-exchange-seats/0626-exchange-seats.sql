# Write your MySQL query statement below
SELECT 
    id,
    CASE 
        -- if odd number then take next id's name
        -- COALESCE: if next line is NULL, keep it's own name
        WHEN id % 2 = 1 THEN COALESCE(LEAD(student, 1) OVER(ORDER BY id), student)
        -- if even number, take last id's name
        ELSE LAG(student, 1) OVER(ORDER BY id)
    END AS student
FROM seat