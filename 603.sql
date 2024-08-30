-- Write your PostgreSQL query statement below

SELECT distinct b1.seat_id 
FROM (SELECT seat_id 
FROM Cinema 
WHERE free = 1) b1 
JOIN (SELECT seat_id 
FROM Cinema 
WHERE free = 1) b2 ON b1.seat_id = b2.seat_id + 1 or b1.seat_id = b2.seat_id - 1;