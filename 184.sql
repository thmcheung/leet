select Department.name AS Department,Employee.name AS Employee,Salary
from Employee JOIN Department ON Employee.DepartmentId = Department.id
where 
(Employee.DepartmentID, Salary) in 
(select departmentID, MAX(salary) 
from Employee 
Group by DepartmentId); 