# Write your MySQL query statement below
select name, unique_id from Employees as e
    left outer join EmployeeUNI as u
    on e.id = u.id