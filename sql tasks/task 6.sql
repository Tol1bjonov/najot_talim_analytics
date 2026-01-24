-- TABLE 1
-- CREATE TABLE customers (
--  customer_id INT PRIMARY KEY,
--  customer_name VARCHAR(80),
--  city VARCHAR(50)
-- );

-- CREATE TABLE shippers (
--  shipper_id INT PRIMARY KEY,
--  shipper_name VARCHAR(80)
-- );

-- CREATE TABLE orders (
--  order_id INT PRIMARY KEY,
--  customer_id INT,
--  shipper_id INT,
--  order_date DATE,
--  total_amount NUMERIC(12,2),
--  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
--  FOREIGN KEY (shipper_id) REFERENCES shippers(shipper_id)
-- );

-- INSERT INTO customers VALUES
-- (1,'Ali Valiyev','Tashkent'),
-- (2,'Dilnoza Karim','Samarkand'),
-- (3,'Kamron Saidov','Bukhara'),
-- (4,'Shahnoza Rahim','Namangan');

-- INSERT INTO shippers VALUES
-- (1,'FastExpress'),
-- (2,'TashPost');

-- INSERT INTO orders VALUES
-- (101,1,1,'2025-10-25',450000),
-- (102,2,2,'2025-10-26',380000),
-- (103,1,1,'2025-10-27',220000),
-- (104,2,2,'2025-10-28',150000);

-- Topshiriqlar
-- A
-- select o.order_id,
-- o.order_date,
-- c.customer_name,
-- s.shipper_name
-- from orders as o
-- inner join shippers as s
-- on o.shipper_id = s.shipper_id
-- inner join customers as c
-- on o.customer_id = c.customer_id
-- B
-- select o.order_id,
-- o.order_date,
-- c.customer_name,
-- s.shipper_name
-- from orders as o
-- left join shippers as s
-- on o.shipper_id = s.shipper_id
-- left join customers as c
-- on o.customer_id = c.customer_id
-- where o.order_id is null
-- C
-- select o.order_id,
-- o.order_date,
-- c.customer_name,
-- s.shipper_name
-- from orders as o
-- right join shippers as s
-- on o.shipper_id = s.shipper_id
-- right join customers as c
-- on o.customer_id = c.customer_id
-- where c.customer_id is null




-- TABLE 2
-- DROP TABLE IF EXISTS employees;
-- DROP TABLE IF EXISTS departments;

-- CREATE TABLE departments (
--  department_id INT PRIMARY KEY,
--  department_name VARCHAR(80)
-- );

-- CREATE TABLE employees (
--  employee_id INT PRIMARY KEY,
--  full_name VARCHAR(80),
--  department_id INT,
--  salary NUMERIC(12,2),
--  FOREIGN KEY (department_id) REFERENCES
-- departments(department_id)
-- );

-- INSERT INTO departments VALUES
-- (1,'HR'),
-- (2,'Finance'),
-- (3,'IT'),
-- (4,'R&D');

-- INSERT INTO employees VALUES
-- (10,'Azizbek Nur',1,9000),
-- (11,'Madina Oqil',2,12000),
-- (12,'Jasur Rav',NULL,8000),
-- (13,'Malika Qodir',3,15000);


-- Topshiriqlar
-- A
-- select e.full_name, d.department_name
-- from departments as d
-- left join employees as e
-- on d.department_id = e.department_id
-- B
-- select e.full_name, d.department_name
-- from employees as e
-- left join departments as d
-- on d.department_id = e.department_id
-- where e.department_id is null
-- C
-- SELECT d.department_name
-- FROM employees AS e
-- RIGHT JOIN departments AS d
-- ON e.department_id = d.department_id
-- WHERE e.department_id IS NULL;



-- TABLE 3
-- CREATE TABLE students (
--  student_id INT PRIMARY KEY,
--  student_name VARCHAR(80),
--  group_name VARCHAR(20)
-- );
-- CREATE TABLE courses (
--  course_id INT PRIMARY KEY,
--  course_name VARCHAR(80),
--  credits INT
-- );
-- CREATE TABLE enrollments (
--  enroll_id INT PRIMARY KEY,
--  student_id INT,
--  course_id INT,
--  enrolled_at DATE,
--  FOREIGN KEY (student_id) REFERENCES students(student_id),
--  FOREIGN KEY (course_id) REFERENCES courses(course_id)
-- );
-- INSERT INTO students VALUES
-- (1,'Bekzod M','DA-01'),
-- (2,'Dilafruz S','DA-01'),
-- (3,'Murod A','DA-02'),
-- (4,'Laylo N','DA-02');
-- INSERT INTO courses VALUES
-- (101,'SQL Advanced',3),
-- (102,'Python for DA',4),
-- (103,'Power BI',2);
-- INSERT INTO enrollments VALUES
-- (1001,1,101,'2025-09-20'),
-- (1002,1,102,'2025-09-21'),
-- (1003,2,101,'2025-09-22'),
-- (1004,3,103,'2025-09-22');

-- Topshiriqlar
-- A
-- select s.student_name, c.course_name, e.enrolled_at
-- from enrollments as e
-- left join courses as c
-- on e.course_id = c.course_id
-- left join students as s
-- on e.student_id = s.student_id
-- B
-- select s.student_name as not_enrolled
-- from students as s
-- left join enrollments as e
-- on s.student_id = e.student_id
-- where e.course_id is null
-- C
-- select c.course_name
-- from courses as c
-- left join enrollments as e
-- on c.course_id = e.course_id
-- where e.course_id is null


-- TABLE 4
-- CREATE TABLE products (
--  product_id INT PRIMARY KEY,
--  product_name VARCHAR(80),
--  price NUMERIC(12,2)
-- );
-- CREATE TABLE orders2 (
--  order_id INT PRIMARY KEY,
--  order_date DATE,
--  customer_note VARCHAR(120)
-- );
-- CREATE TABLE order_items (
--  order_item_id INT PRIMARY KEY,
--  order_id INT,
--  product_id INT,
--  qty INT,
--  FOREIGN KEY (order_id) REFERENCES orders2(order_id),
--  FOREIGN KEY (product_id) REFERENCES products(product_id)
-- );
-- INSERT INTO products VALUES
-- (1,'Laptop 14"',750.00),
-- (2,'Mouse',15.00),
-- (3,'Keyboard',25.00),
-- (4,'Monitor 24"',180.00);
-- INSERT INTO orders2 VALUES
-- (501,'2025-10-20','Urgent'),
-- (502,'2025-10-21','Gift wrap'),
-- (503,'2025-10-22',NULL);
-- INSERT INTO order_items VALUES
-- (9001,501,1,1),
-- (9002,501,2,2),
-- (9003,502,4,1);

-- Topshiriqlar
-- A
-- select 
-- o2.order_id, 
-- o2.order_date, 
-- p.product_name, 
-- o.qty,
-- o.qty * p.price AS line_total
-- from order_items as o
-- inner join orders2 as o2 
-- on o.order_id = o2.order_id
-- inner join products as p
-- on p.product_id = o.product_id
-- B
-- select
-- p.product_name as not_sale
-- from products as p
-- left join order_items as o
-- on p.product_id = o.product_id
-- where o.order_id is null
-- C
-- select 
-- p.product_name,
-- p.price,
-- SUM(o.qty*p.price) as total
-- from products as p
-- inner join order_items as o
-- on p.product_id = o.product_id
-- group by p.product_id, p.product_name, p.price

-- TABLE 5
-- CREATE TABLE authors (
--  author_id INT PRIMARY KEY,
--  author_name VARCHAR(80),
--  country VARCHAR(50)
-- );
-- CREATE TABLE publishers (
--  publisher_id INT PRIMARY KEY,
--  publisher_name VARCHAR(80)
-- );
-- CREATE TABLE books (
--  book_id INT PRIMARY KEY,
--  title VARCHAR(120),
--  author_id INT,
--  publisher_id INT,
--  published_year INT,
--  FOREIGN KEY (author_id) REFERENCES authors(author_id),
--  FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
-- );
-- INSERT INTO authors VALUES
-- (1,'Orhun Bek','Turkey'),
-- (2,'Zulfiya','Uzbekistan'),
-- (3,'George K.','UK');
-- INSERT INTO publishers VALUES
-- (10,'Sahifa Nashr'),
-- (11,'BookLine'),
-- (12,'Global Print');
-- INSERT INTO books VALUES
-- (100,'Data Analytics 101',1,10,2022),
-- (101,'She’rlar To‘plami',2,11,2019),
-- (102,'AI for Everyone',NULL,12,2024);

-- Topshiriqlari
-- A
select
b.title, 
a.author_name, 
p.publisher_name,
b.published_year
from books as b
left join authors as a
on b.author_id = a.author_id
left join publishers as p
on p.publisher_id = b.publisher_id


