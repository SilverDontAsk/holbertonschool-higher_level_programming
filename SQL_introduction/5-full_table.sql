-- creates a table called first_table
first_table CREATE TABLE 'first_table' (
'id' int NOT NULL AUTO_INCREMENT,
'name' varchar(128) DEFAULT NULL,
'c' char(1) DEFAULT NULL,
'created-at' date DEFAULT NULL,
PRIMARY KEY ('id')
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
