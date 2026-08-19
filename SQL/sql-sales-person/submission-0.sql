-- Write your query below
SELECT s.name from sales_person as s where s.name not in (
SELECT s.name from sales_person as s left join company as c left join orders as o on o.com_id = c.com_id on o.sales_id = s.sales_id where c.name = 'CRIMSON')