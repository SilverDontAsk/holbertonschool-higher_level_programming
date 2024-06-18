-- list all cities of California in db hbtn_0d_usa
USE hbtn_0d_usa;
SELECT cities.name
FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;
