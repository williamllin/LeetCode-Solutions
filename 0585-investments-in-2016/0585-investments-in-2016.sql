
#con1: more than one same 2015 investment
#con2: different cities
select round(sum(tiv_2016),2) as tiv_2016
from insurance
where tiv_2015 in (
    select tiv_2015
    from insurance
    group by tiv_2015
    having count(*)>=2
) 
    and (lat, lon) in (
        select lat, lon
        from insurance
        group by lat, lon
        having count(*) = 1
    )