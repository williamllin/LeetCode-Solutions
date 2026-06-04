WITH dayamount AS (
    SELECT visited_on, SUM(amount) AS dailyamount
    FROM customer
    GROUP BY visited_on
),

movingmetrics AS (
    SELECT 
        visited_on,
        SUM(dailyamount) OVER(ORDER BY visited_on ROWS 6 PRECEDING) AS amount,
        ROUND(AVG(dailyamount) OVER(ORDER BY visited_on ROWS 6 PRECEDING), 2) AS average_amount
    FROM dayamount
)

SELECT visited_on, amount, average_amount
FROM movingmetrics
WHERE DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM customer)) >= 6
ORDER BY visited_on ASC;
