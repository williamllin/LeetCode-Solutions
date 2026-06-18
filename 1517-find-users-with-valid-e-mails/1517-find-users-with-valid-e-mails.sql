# Write your MySQL query statement below

#too many conditions, so using where xxx LIKE and xxx NOT LIKE.... won't work

#regular expression
select user_id, name, mail
from users
where mail regexp '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'
    and mail like binary '%@leetcode.com'