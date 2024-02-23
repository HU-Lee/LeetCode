# Write your MySQL query statement below
with tmp as (
    select *,
    (select count(*) from Employee where managerId = e.id) as cnt
    from Employee as e
)
select name from tmp where cnt >= 5