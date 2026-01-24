-- orders jadvali
-- CREATE TABLE orders (
--     order_id     VARCHAR(10),
--     customer     VARCHAR(50),
--     product      VARCHAR(50),
--     quantity     INT
-- );
-- INSERT INTO orders (order_id, customer, product, quantity) 
-- VALUES('023958',  'Пятерочка', 'Яблоки', 11),
-- ('023959', 'Лента', 'Виноград', 15),
-- ('023960',  'Магнит', 'Апельсины', 17),
-- ('023961',  'Пятерочка', 'Бананы', 4 ),
-- ('023962',  'Лента', 'Груши', 17),
-- ('023963',  'Перекресток', 'Виноград', 21 ),
-- ('023964', 'Пятерочка', 'Бананы', 3 ),
-- ('023965',  'Перекресток', 'Виноград', 10 ),
-- ('023966',  'Пятерочка', 'Апельсины', 8 ),
-- ('023967',  'Пятерочка', 'Виноград', 16 ),
-- ('023968',  'Магнит', 'Бананы', 3 ),
-- ('023969', 'Пятерочка', 'Апельсины', 12 ),
-- ('023970', 'Лента', 'Яблоки', 18),
-- ('023971',  'Ашан', 'Груши', 20),
-- ('023972',  'Ашан', 'Груши', 11),
-- ('023973',  'Перекресток', 'Виноград', 10),
-- ('023974',  'Пятерочка', 'Апельсины', 25);

--managers jadvali
-- CREATE TABLE managers (
--     manager VARCHAR(50),
--     order_id VARCHAR(20)
-- );
-- INSERT INTO managers (manager, order_id) VALUES
-- ('Сергеева', '023958'),
-- ('Кузнецов', '023959'),
-- ('Сергеева', '023960'),
-- ('Воронова', '023961'),
-- ('Кузнецов', '023962'),
-- ('Воронова', '023963'),
-- ('Сергеева', '023964'),
-- ('Воронова', '023965'),
-- ('Афанасьев', '023966'),
-- ('Кузнецов', '023967'),
-- ('Кузнецов', '023968'),
-- ('Сергеева', '023969'),
-- ('Воронова', '023970'),
-- ('Афанасьев', '023971'),
-- ('Сергеева', '023972'),
-- ('Кузнецов', '023973'),
-- ('Сергеева', '023974');

-- price_list jadvali
-- CREATE TABLE price_list (
--     product VARCHAR(50),
--     price DECIMAL(10,2)
-- );
-- INSERT INTO price_list (product, price) VALUES
-- ('Апельсины', 100.00),
-- ('Виноград', 150.00),
-- ('Яблоки', 90.00),
-- ('Бананы', 70.00),
-- ('Груши', 140.00);

-- brach jadvali
-- CREATE TABLE branches (
--     city VARCHAR(50),
--     phone VARCHAR(20),
--     manager VARCHAR(50)
-- );
-- INSERT INTO branches (city, phone, manager) VALUES
-- ('Москва', '123-45-67', 'Сергеева'),
-- ('Санкт-Петербург', '890-12-34', 'Кузнецов'),
-- ('Волгоград', '567-89-01', 'Воронова'),
-- ('Мурманск', '234-56-78', 'Афанасьев'),
-- ('Краснодар', '901-23-45', 'Никитина');



select o.order_id, m.manager, o.customer, o.product, o.quantity, p.price, o.quantity * p.price as total_price,  b.city, b.phone
from orders o
inner join managers m
on o.order_id = m.order_id
inner join price_list p
on o.product = p.product
inner join branches b
on m.manager = b.manager






