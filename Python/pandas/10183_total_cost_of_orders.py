# 10183 Total Cost of Orders
import pandas as pd

customers.head()
merged = pd.merge(customers, orders, left_on='id', right_on='cust_id')
merged = merged.groupby(['cust_id', 'first_name'])['total_order_cost'].sum().reset_index()

result = merged.sort_values(by='first_name', ascending=True)