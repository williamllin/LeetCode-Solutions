select st.student_id, st.student_name, su.subject_name, count(e.subject_name) as attended_exams
from students st
    cross join subjects su
    left join examinations e
        on st.student_id = e.student_id
        and su.subject_name = e.subject_name
    
group by  st.student_id, st.student_name, su.subject_name
order by st.student_id, su.subject_name

#count(e.subject_name) so that there's 'NULL' to be displayed as '0'
#cross join makes every students match each subject, doesn't matter if they took it or not











