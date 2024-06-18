-- creates user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- grants privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flushes privileges to apply changes
FLUSH PRIVILEGES;
