select SecondHighestSalary from 
(SELECT 
    (SELECT MAX(Salary) 
     FROM Employee) AS Highest,
    (SELECT MAX(Salary) 
     FROM Employee 
     WHERE Salary < (SELECT MAX(Salary) FROM Employee)) AS SecondHighestSalary,
    MAX(Salary) AS ThirdHighest
FROM Employee 
WHERE Salary < 
    (SELECT MAX(Salary) 
     FROM Employee 
     WHERE Salary < (SELECT MAX(Salary) FROM Employee))) a
