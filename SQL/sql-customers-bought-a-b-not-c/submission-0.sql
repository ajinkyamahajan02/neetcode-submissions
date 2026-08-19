-- Write your query below
SELECT c.customer_id, c.customer_name from customers as c where c.customer_id in (
    select customer_id from orders where product_name = 'A'
) AND 

c.customer_id in (
    select customer_id from orders where product_name = 'B'
)

AND c.customer_id not in (
    select customer_id from orders where product_name = 'C'
)

Order by c.customer_name 