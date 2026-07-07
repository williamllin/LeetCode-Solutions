select user_id, 
    concat(
        upper(left(name, 1)), #left 1st
        lower(substring(name, 2)) #the rest since 2nd
    ) as name
from users
order by user_id