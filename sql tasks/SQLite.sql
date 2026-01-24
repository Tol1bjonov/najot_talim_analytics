-- Birinchi table
CREATE TABLE coffee_sales (
	id SERIAL,
  	drink_name VARCHAR(50),
  	size CHAR(1),
  	price INT,
  	city VARCHAR(50),
  	date DATE
);

INSERT INTO coffee_sales (drink_name, size, price, city, date)
VALUES
('Latte', 'M', 25000, 'Tashkent', '2025-10-10'),
('Americano', 'L', 27000, 'Samarkand', '2025-10-10'),
('Latte', 'S', 20000, 'Tashkent', '2025-10-10'),
('Latte', 'M', 18000, 'Tashkent', '2025-10-10'),
('Latte', 'L', 30000, 'Andijan', '2025-10-10');

SELECT * FROM coffee_sales;
SELECT * FROM coffee_sales
WHERE city = 'Tashkent';
SELECT * FROM coffee_sales
WHERE price > 25000;
SELECT * FROM coffee_sales
WHERE date = '2025-10-11';



--Ikkinchi jadval
CREATE TABLE students (
    id SERIAL,
    full_name VARCHAR(50),
    course VARCHAR(50),
    progress INT,
    city VARCHAR(50)
);
INSERT INTO students (full_name, course, progress, city)
VALUES
('Jasmina Nurova', 'Data Analytics', 95, 'Tashkent'),
('Bekzod Karimov', 'Python', 65, 'Samarkand'),
('Dilnoza Karimova', 'Data Analytics', 80, 'Bukhara'),
('Oybek Islomov', 'Design', 45, 'Tashkent'),
('Alihan G‘aniev', 'Data Analytics', 70, 'Andijan');

-- 1-shart
SELECT * FROM students
WHERE course = 'Data Analytics';
-- 2-shart
SELECT * FROM students
WHERE progress > 70;
-- 3-shart
SELECT * FROM students
WHERE city = 'Tashkent' AND progress > 90;



-- Uchinchi jadval
CREATE TABLE orders (
    id SERIAL,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price INT,
    payment_type VARCHAR(20)
);
INSERT INTO orders (product_name, category, price, payment_type)
VALUES
('Headphones', 'Electronics', 190000, 'Card'),
('Notebook', 'Stationery', 35000, 'Cash'),
('Powerbank', 'Electronics', 220000, 'Card'),
('Bag', 'Accessories', 50000, 'Cash'),
('Mouse', 'Electronics', 85000, NULL);

SELECT * FROM orders
WHERE price > 100000;

SELECT * FROM orders
WHERE payment_type = 'Card';
 
SELECT * FROM orders
WHERE payment_type IS NULL;



-- Tortinchi jadval
CREATE TABLE bus_passengers (
  id SERIAL,
  route INT,
  passenger_name VARCHAR(100),
  ticket_price INT,
  time TIME       
);

INSERT INTO bus_passengers (id, route, passenger_name, ticket_price, time)
VALUES
(1, 17, 'Azizbek Olimov',   5000, '07:30'),
(2, 28, 'Jasur Bekov',      6000, '09:00'),
(3, 17, 'Oybek Raximov',    5000, '17:30'),
(4, 44, 'Madina Karimova',  8000, '08:00'),
(5, 17, 'Laylo Rustamova',  5000, '07:45');

SELECT * FROM bus_passengers
WHERE route = 17;

SELECT * FROM bus_passengers
WHERE ticket_price < 6000;

SELECT * FROM bus_passengers
WHERE time BETWEEN '07:00' AND '08:00';




--Beshinchi jadval 
CREATE TABLE warehouse (
  id INT PRIMARY KEY,
  product_name VARCHAR(50),
  quantity INT,
  supplier VARCHAR(50),
  last_update DATE
);
INSERT INTO warehouse (id, product_name, quantity, supplier, last_update)
VALUES
(1, 'Sugar', 120, 'AgroFarm', '2025-10-10'),
(2, 'Rice', 50, 'MillFood', '2025-10-09'),
(3, 'Flour', 180, 'AgroFarm', '2025-10-11'),
(4, 'Oil', 75, 'FoodLine', '2025-10-12'),
(5, 'Tea', 25, NULL, '2025-10-11');

SELECT * FROM warehouse
WHERE supplier = 'AgroFarm'; 

SELECT * FROM warehouse
WHERE quantity < 100;

SELECT * FROM warehouse
WHERE supplier IS NULL;




