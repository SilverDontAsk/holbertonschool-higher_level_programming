-- creates database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- sets current db to previously created db
USE hbtn_0d_usa;

-- create table cities
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
	);
