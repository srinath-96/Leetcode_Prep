# Write your MySQL query statement below
select name,balance from (select name,SUM(amount) as balance from Users a right join Transactions b on a.account=b.account
group by a.account)c 
where balance>10000
