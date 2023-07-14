INSERT INTO users
(first_name, last_name)
VALUES ('Jane','Amsden'), 
('Emily', 'Dixon'),
('Theodore', 'Dostoevsky'),
('William', 'Shapiro'),
('Lao', 'Xiu');

select * from users;

INSERT INTO books
(title)
VALUES
('C Sharp'),
('Java'),
('Python'),
('PHP'),
('Ruby');

select * from books;

UPDATE books
SET title = 'C#'
WHERE id = 1;

UPDATE users
SET first_name = 'Bill'
WHERE id = 4;

INSERT INTO favorites
(user_id, book_id)
VALUES
(1,1),
(1,2);

select * from favorites;

INSERT INTO favorites
(user_id, book_id)
VALUES
(2,1),
(2,2),
(2,3);


INSERT INTO favorites
(user_id, book_id)
VALUES
(3,1),
(3,2),
(3,3),
(3,4);

INSERT INTO favorites
(user_id, book_id)
VALUES
(4,1),
(4,2),
(4,3),
(4,4),
(5,5);

SELECT users.id, users.first_name, users.last_name, favorites.book_id as 'favorite_book' FROM USERS
INNER JOIN favorites
on users.id = favorites.user_id
WHERE book_id=3;

DELETE FROM favorites 
WHERE user_id = 2 AND book_id = 3

INSERT INTO favorites
(user_id, book_id)
VALUES
(5,2);

SELECT u.id, u.first_name, u.last_name, b.book_id, b.title FROM USERS u
INNER JOIN favorites f
on u.id = f.user_id
INNER JOIN books b
on b.id = f.book_id
WHERE u.id = 3;


SELECT u.id as 'user_id', u.first_name, u.last_name, f.book_id, b.title FROM USERS u
INNER JOIN favorites f
on u.id = f.user_id
INNER JOIN books b
on b.id = f.book_id
WHERE f.book_id = 5;
