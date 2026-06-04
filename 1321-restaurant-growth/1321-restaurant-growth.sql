# Write your MySQL query statement below
WITH DailyAmount AS (
    SELECT visited_on, SUM(amount) AS day_amount
    FROM Customer
    GROUP BY visited_on
),

MovingMetrics AS (
    SELECT 
        visited_on,
        #sum of today + last 6
        SUM(day_amount) OVER(ORDER BY visited_on ROWS 6 PRECEDING) AS amount,
        #7 days average
        ROUND(AVG(day_amount) OVER(ORDER BY visited_on ROWS 6 PRECEDING), 2) AS average_amount,
        #put number on days, since first 6 days need to be filtered
        ROW_NUMBER() OVER(ORDER BY visited_on) AS rn
    FROM DailyAmount
)
SELECT visited_on, amount, average_amount
FROM MovingMetrics
WHERE rn >= 7
ORDER BY visited_on ASC;