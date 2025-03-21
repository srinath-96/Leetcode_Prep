# Write your MySQL query statement below
select b.name as Department,a.name as Employee,a.salary as Salary  from Employee a left join Department b on a.departmentID=b.id
where (b.id,a.salary) in (select b.id,MAX(salary) 
           OVER (PARTITION BY b.name) from Employee a  join Department b on a.departmentID=b.id )