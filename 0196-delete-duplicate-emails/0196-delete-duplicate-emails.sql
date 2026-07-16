
delete from person
where id not in(
    select t.min_id
    from(
        select min(id) as min_id
        from person
        group by email
    )t
)
#Cannot select table while delete/update from table
#so create table t