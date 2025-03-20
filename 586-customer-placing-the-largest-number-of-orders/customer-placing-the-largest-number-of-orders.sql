# Write your MySQL query statement below
select customer_number from (select customer_number,Count(customer_number) as t from Orders
group by customer_number
order by t DESC  ) a
limit 1



