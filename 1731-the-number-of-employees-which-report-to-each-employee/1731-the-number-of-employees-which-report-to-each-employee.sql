# Write your MySQL query statement below
with tmp as (
    select reports_to,
    count(name) as reports_count,
    round(avg(age)) as average_age
    from Employees
    where reports_to is not null
    group by reports_to 
) 
select 
    e.employee_id,
    e.name,
    tmp.reports_count,
    tmp.average_age
from tmp
join Employees e
on e.employee_id = tmp.reports_to
order by e.employee_id