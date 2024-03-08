# Write your MySQL query statement below
with tmp as (
    select p.product_id, u.units, p.price
from Prices p
left join UnitsSold u
on p.product_id = u.product_id
where (u.purchase_date between p.start_date and p.end_date) or u.units is null
)
select product_id,
ifnull(round(sum(units*price)/sum(units),2),0) as average_price
from tmp
group by product_id