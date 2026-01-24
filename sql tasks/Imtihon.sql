-- 1-topshiriq
-- select p.product_name, 
--  sum(s.quantity) as summa
-- from products as p 
-- inner join sales as s
-- on p.product_id = s.product_id
-- group by p.product_name
-- order by summa desc  limit 3

--2-topshiriq
-- select d.full_name, sum(o.distance_km) as total_km, sum(o.price) as total_sum
-- from orders o
-- inner join drivers d
-- on o.driver_id = d.driver_id
-- where o.distance_km > 10
-- group by d.full_name
-- order by total_km, total_sum

-- 3-topshiriq
-- 3.1
-- select room_type, sum(nights) as total_nights 
-- from  bookings
-- group by room_type

-- 3.2
-- select room_type, sum(nights) as total_nights 
-- from  bookings
-- group by room_type
-- having sum(nights) > 5;

-- 4-topshiriq
-- 4.1
-- update deliveries
-- set price = weight_kg * 5000;

--4.2
-- select c.full_name, d.weight_kg, d.price, d.delivery_date
-- from deliveries d
-- inner join customers c 
-- on d.customer_id = c.customer_id
-- where d.status = 'delivered'
-- order by d.weight_kg desc
-- limit 2;

-- 5-topshiriq
-- with last_orders as (
--     select 
-- 		u.full_name,
--         o.order_date,
--         row_number() over (partition by u.full_name order by o.order_date desc) as rn
--     from orders o
-- 	inner join users u
-- 	on u.user_id = o.user_id
-- )
-- select full_name, order_date as last_order_date
-- from last_orders
-- where rn = 1
-- order by order_date;

