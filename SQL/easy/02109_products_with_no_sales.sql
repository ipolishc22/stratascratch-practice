-- 2109 products with no sales
SELECT p.prod_sku_id, p.market_name
FROM fct_customer_sales s
RIGHT JOIN dim_product p ON p.prod_sku_id = s.prod_sku_id
WHERE s.prod_sku_id IS NULL;