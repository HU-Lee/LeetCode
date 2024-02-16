with t as (
    select *,
    lag(temperature, 1) over(order by recordDate) as prev_temperature,
    lag(recordDate, 1) over(order by recordDate) as prev_date
    from Weather
) 
select t.id from t 
where t.temperature > t.prev_temperature
and t.prev_date = t.recordDate - INTERVAL 1 DAY 