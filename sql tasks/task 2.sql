-- create table orders2(
-- 	id serial,
-- 	item_name text,
-- 	quantity int,
-- 	price int,
-- 	order_date timestamp
-- );

-- INSERT INTO orders2 (item_name, quantity, price, order_date) VALUES
-- ('Zinger', 2, 25000, '2025-06-01 13:00:00'),
-- ('Twister', 1, 22000, '2025-06-01 15:45:00'),
-- ('Strips', 3, 18000, '2025-06-02 12:20:00'),
-- ('Pepsi', 2, 7000, '2025-06-02 12:25:00'),
-- ('Zinger', 1, 25000, '2025-06-03 10:15:00'),
-- ('Twister', 2, 22000, '2025-06-03 19:00:00'),
-- ('Bucket', 1, 75000, '2025-06-04 18:30:00'),
-- ('Strips', 2, 18000, '2025-06-05 11:10:00'),
-- ('Pepsi', 1, 7000, '2025-06-06 14:00:00'),
-- ('Zinger', 1, 25000, '2025-06-06 17:45:00'),
-- ('Twister', 1, 22000, '2025-06-07 20:00:00'),
-- ('Bucket', 1, 75000, '2025-06-08 13:30:00'),
-- ('Strips', 1, 18000, '2025-06-08 15:00:00'),
-- ('Pepsi', 3, 7000, '2025-06-09 11:00:00'),
-- ('Zinger', 1, 25000, '2025-06-09 16:45:00');

-- 1-topshiriq
-- SELECT *
-- FROM orders2
-- ORDER BY order_date DESC
-- LIMIT 5;

-- 2-topshiriq
-- select * from orders2
-- order by price desc
-- limit 5

-- 3-topshiriq
-- select * from orders2
-- order by price asc
-- limit 3

-- 4-topshiriq
-- select * from orders2
-- order by quantity desc
-- limit 3

-- 5-topshiriq
select *
from orders2
where item_name = 'Zinger'
order by order_date asc;

	




