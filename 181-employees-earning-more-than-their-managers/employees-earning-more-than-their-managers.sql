# Write your MySQL query statement below
select f.name as Employee from Employee e join Employee f on e.id=f.managerID where f.salary>e.salary
