-- create table bank_accounts(
-- 	account_id serial,
-- 	branch_name text,
-- 	account_type text,
-- 	balance int
-- )

-- insert into bank_accounts(branch_name, account_type, balance)
-- values('Tashkent', 'Savings', 32000000),
-- ('Samarkand', 'Current', 15000000),
-- ('Tashkent', 'Current', 28000000),
-- ('Bukhara', 'Savings', 21000000),
-- ('Bukhara', 'Current', 12000000)

-- select * from bank_accounts


-- 1-task
-- select branch_name, count(*) as num_accounts,
-- avg(balance) as avg_balance
-- from bank_accounts
-- group by branch_name




-- 2 - jadval
-- create table rides(
-- 	ride_id serial,
-- 	driver_id varchar(10),
-- 	city varchar(30),
-- 	distance int,
-- 	fare int
-- )

-- insert into rides(driver_id, city, distance, fare)
-- values('D001', 'Tashkent', 8, 28000),
-- ('D001', 'Tashkent', 12, 34000),
-- ('D001', 'Samarkand', 10, 32000),
-- ('D003', 'Bukhara', 15, 40000),
-- ('D002', 'Tashkent', 6, 20000)

-- select driver_id, sum(distance) as total_distance,
-- sum(fare) as total_fare
-- from rides
-- group by driver_id


-- 3 jadval
-- create table course_results(
-- 	student_id serial,
-- 	course_name varchar(20),
-- 	score int
-- )

-- insert into course_results(course_name, score)
-- values('python', 85),
-- ('sql', 90),
-- ('power bi', 78),
-- ('sql', 70),
-- ('python', 95),
-- ('power bi', 82)

-- select course_name, avg(score) as avg_score,
-- max(score) as max_score
-- from course_results
-- group by course_name




-- 4-jadval
-- create table hospital_visits(
-- 	visit_id serial,
-- 	department varchar(20),
-- 	doctor_name varchar(20),
-- 	visit_fee int
-- )

-- insert into hospital_visits(department, doctor_name, visit_fee)
-- values('Cardiology',  'Dr. Karimov', 150000),
-- ('Neurology',  'Dr. Rashidov', 200000),
-- ('Cardiology',  'Dr. Karimov', 180000),
-- ('Pediatrics',  'Dr. Zokirova', 120000),
-- ('Neurology',  'Dr. Rashidov', 220000)

-- select department, min(visit_fee) as min_fee,
-- max(visit_fee) as max_fee
-- from hospital_visits
-- group by department





-- 5 jadval
-- create table social_posts(
-- 	post_id serial, 
-- 	user_id varchar(10),
-- 	platform varchar(20),
-- 	likes int,
-- 	comments int
-- )

-- insert into social_posts(user_id, platform, likes, comments)
-- values('U001',  'Instagram', 340, 25),
-- ('U002',  'Telegram', 120, 10),
-- ('U001',  'Instagram', 410, 50),
-- ('U003',  'YouTube', 950, 80),
-- ('U002',  'Telegram', 150, 15)


select platform, sum(likes) as total_likes,
avg(comments) as avg_comment, count(*) as post_count
from social_posts
group by platform

