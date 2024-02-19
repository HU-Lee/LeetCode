# Write your MySQL query statement below
with tmp as (
    select machine_id,
    case when activity_type='start' then -timestamp
        else timestamp
    end as time_tmp
    from Activity
) select tmp.machine_id as machine_id,
    round(avg(tmp.time_tmp) * 2, 3) as processing_time
    from tmp
    group by tmp.machine_id