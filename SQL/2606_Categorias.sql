SELECT p.id, p.name 
FROM products p 
INNER JOIN categories c
on p.id_categories = c.id
WHERE c.name like 'super%';