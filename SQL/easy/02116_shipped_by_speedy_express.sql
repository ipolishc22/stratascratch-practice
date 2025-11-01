-- 2116 shipped by speedy express
SELECT COUNT(DISTINCT o.order_id) AS order_count
FROM shopify_orders o
JOIN shopify_carriers c ON o.carrier_id = c.id
WHERE c.name = "Speedy Express";