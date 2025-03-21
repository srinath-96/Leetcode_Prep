# Write your MySQL query statement below
select score, Dense_rank() over (order by score Desc) as 'rank'  from Scores