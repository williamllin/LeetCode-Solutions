select user_id,
    concat(
        upper(left(name,1)), #left 1st letter
        lower(substring(name,2)) #the rest letters since 2nd
    ) as name
from users
order by user_id