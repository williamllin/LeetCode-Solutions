# Write your MySQL query statement below
/*
select v.customer_id, count(customer_id) as count_no_trans
from visits v
    left join transactions t
        on v.visit_id = t.visit_id
where t.transaction_id is NULL
group by v.customer_id

#visit id/custom id/tran id
#1       /23       /12
#2       /9        /13
#4       /30*      /null
#5       /54       /2
#5       /54       /3
#5       /54       /9
#6       /96*      /null
#7       /54*      /null
#8       /54*      /null
*/
select v.customer_id, count(v.customer_id) as count_no_trans
from visits v
    left join transactions t
        on v.visit_id = t.visit_id
where t.transaction_id is null       
group by v.customer_id

/*
vid/cusid/tid

1 23 12
2 09 13
4 30 xx
5 54 02
5 54 03
5 54 09
6 96 xx
7 54 xx
8 54 xx
*/










