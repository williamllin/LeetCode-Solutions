# Write your MySQL query statement below
select w1.id
from weather w1
    join weather w2
        on datediff(w1.recorddate, w2.recorddate) =1 #w1 2015-01-02 match w2 2015/01/01
where w1.temperature > w2.temperature