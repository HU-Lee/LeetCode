# Write your MySQL query statement below
with c_tmp as (
    select 
        user_id,
        count(*) as tot_count,
        sum(case when action = 'confirmed' then 1 else 0 end) as acc_count
    from Confirmations
    group by user_id 
) 
select s.user_id,
    round(ifnull(c.acc_count/c.tot_count, 0), 2) as confirmation_rate
from Signups s
left join c_tmp c
on c.user_id = s.user_id