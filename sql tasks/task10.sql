-- CREATE TABLE employees2 (
--     emp_id INT,
--     full_name VARCHAR(50),
--     department VARCHAR(50),
--     salary NUMERIC
-- );

-- INSERT INTO employees2 VALUES
-- (1, 'Azizbek Nur', 'IT', 15000000),
-- (2, 'Madina Qodirova', 'IT', 12000000),
-- (3, 'Jasur Aliyev', 'Finance', 9000000),
-- (4, 'Malika To‘xtayeva', 'Finance', 11000000),
-- (5, 'Nodirbek Usmonov', 'Marketing', 8000000),
-- (6, 'Gulbahor Yo‘ldosheva', 'Marketing', 9500000);

-- 1
-- select *,
-- rank() over(partition by department order by salary desc) as rating
-- from employees2

-- 2
-- select * 
-- from (select *,
-- rank() over(partition by department order by salary desc) as rating
-- from employees2)
-- where rating = 1

-- 3
select department,
max(salary) - min(salary) as salary_diff
from employees2
group by department
order by salary_diff desc
limit 1



