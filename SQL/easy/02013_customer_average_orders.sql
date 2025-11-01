-- 2013 customer average orders
SELECT COUNT(DISTINCT customer_id) AS customer_count, AVG(amount) AS avg_order_amount
FROM postmates_orders;