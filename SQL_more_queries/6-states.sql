-- creates database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to newly created db
USE hbtn_0d_usa;

-- create table states in previously created database
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
	name VARCHAR(256) NOT NULL
	);
