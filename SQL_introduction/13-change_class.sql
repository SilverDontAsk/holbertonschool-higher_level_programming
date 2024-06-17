-- removes the rows with scores equal to or below 5 then prints the rest
UPDATE second_table SET score = 10 WHERE name = 'Bob';
DELETE FROM second_table WHERE score <= 5;
