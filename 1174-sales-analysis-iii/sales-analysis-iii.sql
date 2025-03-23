# Write your MySQL query statement below
select a.product_id,product_name
 from Sales a left join Product b on a.product_id=b.product_id
group by a.product_id
Having min(sale_date)>="2019-01-01" and max(sale_date)<="2019-03-31"