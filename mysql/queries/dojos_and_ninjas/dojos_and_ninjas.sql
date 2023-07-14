INSERT INTO dojos(dojos.name)
VALUE
('Dojo1'),
('Dojo2'),
('Dojo3');

SET SQL_SAFE_UPDATES = 0;

DELETE FROM dojos;

INSERT INTO dojos(dojos.name)
VALUE
('YoseKAI'),
('EikenKAI'),
('ButokuDEN');

SELECT * FROM dojos;

INSERT INTO ninjas(dojo_id, first_name, last_name, age)
VALUE
(4, 'Immanuel', 'Vattakunnel', 29),
(4, 'John', 'Smith', 33),
(4, 'Tony', 'Finch', 24);

SELECT * FROM ninjas;

INSERT INTO ninjas(dojo_id, first_name, last_name, age)
VALUE
(5, 'Adrian', 'Sanchez', 25),
(5, 'Andrew', 'Flint', 34),
(5, 'Lebron', 'James', 39);

SELECT * FROM ninjas;

INSERT INTO ninjas(dojo_id, first_name, last_name, age)
VALUE
(6, 'Ryan', 'Parker', 36),
(6, 'Vincent', 'Stone', 21),
(6, 'Angela', 'White', 27);

SELECT * FROM ninjas;

SELECT * FROM ninjas
WHERE dojo_id = 4;

SELECT * FROM ninjas
WHERE dojo_id = 6;

SELECT ninjas.first_name, ninjas.last_name, ninjas.age, dojos.name as 'dojo_name'
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 9;


SELECT *
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 6;

SELECT *
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id