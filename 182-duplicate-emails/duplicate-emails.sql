# Write your MySQL query statement below
select email from (select id,email,Count(email) as a2 from Person
group by email) a 
where a2>1