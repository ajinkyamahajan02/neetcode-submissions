-- Write your query below
SELECT sp.name from sales_person as sp where sp.sales_id not in (
SELECT o.sales_id from orders as o join company c on o.com_id = c.com_id where c.name = 'CRIMSON')