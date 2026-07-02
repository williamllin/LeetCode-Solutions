with preparedtable as (
    select num,
        lead(num, 1)over(order by id) as nextnum, #lead()over... will move down the column to scan
        lead(num, 2)over(order by id) as nextnextnum
    from logs
)
select distinct num as ConsecutiveNums
from preparedtable
where num = nextnum and num = nextnextnum
