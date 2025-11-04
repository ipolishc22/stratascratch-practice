# 10552 identify never sold inventory products
import pandas as pd 

sales_transactions.head()

sold_product_ids = sales_transactions[sales_transactions['quantity_sold'] > 0]['product_id'].unique()
unsold_products = inventory_current_stock[~inventory_current_stock['product_id'].isin(sold_product_ids)]
result = unsold_products[['product_id', 'product_name']]
result