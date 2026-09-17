CREATE database IF NOT EXISTS ibm_hr ;
USE ibm_hr;
select * from employees;
-- Q1. Which employees have a MonthlyIncome below 5,000?
select * from employees where MonthlyIncome <= 5000;

-- Q2. Which employees have a PercentSalaryHike greater than 10%?
select * from employees where PercentSalaryHike > 10;

-- Q3. How many female employees have left the company?
Select count(Gender) AS Fem_Attrition from employees where Attrition = "Yes" And Gender = "Female";

-- Q4. How many male employees have left the company?
Select count(Gender) AS Male_Attrition from employees where Attrition = "Yes" And Gender = "Male";

-- Q5. Among female employees who left the company, which employee(s)
-- have the greatest DistanceFromHome?
Select * from employees where Attrition = "Yes" And Gender = "Female" And DistanceFromHome = 
(select max(DistanceFromHome) from employees where Attrition = "Yes"
And Gender = "Female"); 
      
-- Q6. Which JobRole has the highest number of employees who left the company?
select JobRole, count(*) As Attrition_Count from employees where Attrition="Yes" group by JobRole
order by Attrition_Count desc limit 1 ;

-- Q7. Among employees in the JobRole with the highest attrition,
-- how does BusinessTravel relate to employee attrition?
select BusinessTravel,Attrition, count(*) as Employee_Count
from employees
where JobRole = (select JobRole from employees where Attrition = "Yes"
 group by JobRole order by count(*) desc limit 1) group by BusinessTravel, Attrition;

-- Q8. Is the attrition rate higher among employees with
-- JobSatisfaction and JobInvolvement below 3 compared with other employees?
select case when JobSatisfaction < 3 and JobInvolvement < 3 then "low involvment & low satisfaction"
else "other employees" end as emp_grp,
count(*) as total_emp, avg ( case when Attrition = "Yes" then 1 else 0 end ) * 100 as attrition_rate
from employees group by emp_grp;



-- Q9. Among employees who left the company, which employees are
-- above 35 years old and belong to the JobRole with the highest attrition?
 select * from employees where Age>35 and Attrition="Yes" and JobRole = (select JobRole from employees 
 where Attrition = "Yes" group by JobRole order by  count(*)desc limit 1) order by age desc;
