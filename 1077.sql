select project_id, p1.employee_id
from Project p1 join Employee
on p1.employee_id = Employee.employee_id
where experience_years = (
    select max(experience_years)
    from Project p2 join Employee
    on p2.employee_id = Employee.employee_id
    where p2.project_id = p1.project_id
);
