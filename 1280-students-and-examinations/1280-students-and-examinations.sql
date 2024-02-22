# Write your MySQL query statement below
with tmp1 as (
    select * from Students as s1
    cross join Subjects as s2
    order by s1.student_id, s2.subject_name
) 
select tmp1.*,
 (select count(*) from Examinations as e 
    where tmp1.student_id = e.student_id
    and tmp1.subject_name  = e.subject_name ) as attended_exams 
from tmp1