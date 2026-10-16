# Write your MySQL query statement below
select 
d.name as Department,
e.name as Employee,
e.salary as Salary
from Employee e
inner join Department d on e.departmentId=d.id
where 3>(
    select count(distinct t.Salary)
    from Employee t
    where t.salary>e.salary
    and e.DepartmentId=t.DepartmentId
)