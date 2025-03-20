# Write your MySQL query statement below
select actor_id,director_id from (select actor_id,director_id,Concat(actor_id,",",director_id) as a, Count(Concat(actor_id,director_id)) as c from ActorDirector
group by a) b where c>=3