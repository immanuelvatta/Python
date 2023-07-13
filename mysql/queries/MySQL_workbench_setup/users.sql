-- selecting everything from a table  
SELECT * FROM names;

-- inserting items into table
INSERT INTO NAMES (name, created_at, updated_at)
Values ('Immanuel Vattakunnel', '2023-07-09 10:34:09', '2023-07-09 15:34:09');

-- inserting multiple items into the table
INSERT INTO NAMES (name, created_at, updated_at)
Values 
('John Smith', '2023-07-09 11:34:09', '2023-07-09 12:34:09'),
('Adam Smith', '2023-07-09 11:22:09', '2023-07-09 11:22:09');

-- updating items in the table
UPDATE names
set 
name = 'Jonathan Smith'
where 
id = 2;

-- deleting items from table
delete from names where
id = 3;