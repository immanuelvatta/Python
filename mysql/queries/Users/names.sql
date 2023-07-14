INSERT INTO names(first_name, last_name, email)
VALUES 
('Immanuel', 'Vattakunnel' , 'immanuelvatta@gmail.com'),
('John', 'Smith', 'johnsmith@example.com'),
('Lebron', 'James', 'lebronjames@nike.com');

SELECT * FROM names;

SELECT * FROM names WHERE email = 'immanuelvatta@gmail.com';

SELECT * FROM names WHERE id = "3";

UPDATE names
SET last_name = 'Pancakes'
WHERE id = 3;

DELETE FROM names WHERE id = 2;

SELECT * FROM names ORDER BY first_name ;
SELECT * from names ORDER BY first_name DESC;