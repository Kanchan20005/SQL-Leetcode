# Write your MySQL query statement below
SELECT name 
FROM 
EMPLOYEE 
WHERE id in 
(SELECT managerId FROM
(SELECT managerId,name,  COUNT(*) OVER (Partition by managerId) as empid
FROM Employee) managers WHERE empid >=5);