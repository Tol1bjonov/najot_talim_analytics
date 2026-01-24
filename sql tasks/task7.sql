-- CREATE TABLE products(
--  product_id INT PRIMARY KEY,
--  product_name VARCHAR(80) NOT NULL,
--  category VARCHAR(40) NOT NULL,
--  unit_price DECIMAL(10,2) NOT NULL
-- );
-- CREATE TABLE customers(
--  customer_id INT PRIMARY KEY,
--  full_name VARCHAR(80) NOT NULL,
--  city VARCHAR(40)
-- );
-- CREATE TABLE online_orders(
--  order_id INT PRIMARY KEY,
--  order_date DATE NOT NULL,
--  customer_id INT NOT NULL,
--  product_id INT NOT NULL,
--  quantity INT NOT NULL CHECK (quantity > 0),
--  channel VARCHAR(10) DEFAULT 'online',
--  CONSTRAINT fk_online_cust FOREIGN KEY (customer_id) REFERENCES
-- customers(customer_id),
--  CONSTRAINT fk_online_prod FOREIGN KEY (product_id) REFERENCES
-- products(product_id)
-- );
-- CREATE TABLE store_orders(
--  order_id INT PRIMARY KEY,
--  order_date DATE NOT NULL,
--  customer_id INT NOT NULL,
--  product_id INT NOT NULL,
--  quantity INT NOT NULL CHECK (quantity > 0),
--  channel VARCHAR(10) DEFAULT 'store',
--  CONSTRAINT fk_store_cust FOREIGN KEY (customer_id) REFERENCES
-- customers(customer_id),
--  CONSTRAINT fk_store_prod FOREIGN KEY (product_id) REFERENCES
-- products(product_id)
-- );

-- Kadrlar tahlili uchun jadvallar
-- CREATE TABLE employees_2024(
--  emp_id INT PRIMARY KEY,
--  full_name VARCHAR(80),
--  dept VARCHAR(40)
-- );
-- CREATE TABLE employees_2025(
--  emp_id INT PRIMARY KEY,
--  full_name VARCHAR(80),
--  dept VARCHAR(40)
-- );

-- INSERT INTO products VALUES
-- (1, 'SQL Starter Course', 'Course', 199000.00),
-- (2, 'Python Basics', 'Course', 249000.00),
-- (3, 'Excel Pro Toolkit', 'Bundle', 179000.00),
-- (4, 'Data Viz Masterclass', 'Course', 299000.00),
-- (5, 'Power BI Dashboard', 'Template', 149000.00);
-- INSERT INTO customers VALUES
-- (101, 'Olimov Jasur', 'Tashkent'),
-- (102, 'Karimova Dilnoza', 'Samarkand'),
-- (103, 'Nazarov Bekzod', 'Bukhara'),
-- (104, 'Shirinova Aziza', 'Tashkent'),
-- (105, 'Rasulov Anvar', 'Fergana');
-- ONLINE orders
-- INSERT INTO online_orders VALUES
-- (10001, '2025-10-01', 101, 1, 1, 'online'),
-- (10002, '2025-10-02', 102, 2, 1, 'online'),
-- (10003, '2025-10-02', 103, 3, 2, 'online'),
-- (10004, '2025-10-03', 101, 2, 1, 'online'),
-- (10005, '2025-10-04', 104, 4, 1, 'online'),
-- (10006, '2025-10-05', 105, 5, 3, 'online'),
-- (10007, '2025-10-05', 101, 5, 1, 'online');
-- STORE orders (bitta dublikat bilan – tahlil uchun)
-- INSERT INTO store_orders VALUES
-- (20001, '2025-10-01', 103, 1, 1, 'store'),
-- (20002, '2025-10-02', 104, 3, 1, 'store'),
-- (20003, '2025-10-03', 101, 1, 1, 'store'),
-- (20004, '2025-10-03', 105, 2, 1, 'store'),
-- (20005, '2025-10-04', 102, 4, 1, 'store'),
-- (20006, '2025-10-05', 101, 5, 1, 'store'),
-- (20007, '2025-10-05', 101, 5, 1, 'store');
-- Employees (INTERSECT/EXCEPT uchun)
-- INSERT INTO employees_2024 VALUES
-- (1, 'Shodiev M', 'Sales'),
-- (2, 'Akbarova N', 'Ops'),
-- (3, 'Ismoilov B', 'IT'),
-- (4, 'Gafurova Z', 'Marketing');
-- INSERT INTO employees_2025 VALUES
-- (3, 'Ismoilov B', 'IT'),
-- (4, 'Gafurova Z', 'Marketing'),
-- (5, 'Jurayev F', 'Ops'),
-- (6, 'Qodirova D', 'Sales');



-- Mashqlari
-- 1
-- SELECT order_id, order_date, customer_id, product_id, quantity, channel FROM  online_orders 
-- UNION ALL 
-- SELECT order_id, order_date, customer_id, product_id, quantity, channel  FROM store_orders
-- order by order_date, order_id

-- 2
SELECT c.customer_id, c.full_name, c.city
from customers as c
join(
	select customer_id from online_orders
	intersect
	select customer_id from store_orders
) as ikkala_dokondan
on c.customer_id = ikkala_dokondan.customer_id












































