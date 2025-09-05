# Write your MySQL query statement below
select email from (select email, Count(email) as c from Person group by email) a
where a.c>1