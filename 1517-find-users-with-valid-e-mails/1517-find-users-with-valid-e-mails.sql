# ^, $ : start, end of string
# [a-zA-Z] : first word
# [a-zA-Z0-9_.-]* : words following the first, * means can be any length
# \\. : since '.' has special meaning so add \\ to transform back to normal '.'
/*
select user_id, name, mail
from users
where mail regexp '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'
    and mail like binary '%@leetcode.com'
*/
select user_id, name, mail 
from users
where mail regexp "^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$"
    and mail like binary "%leetcode.com" #binary: case sensitive