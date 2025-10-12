# 9891 Customer Details 
import pandas as pd

customers.head()

merged = pd.merge(customers, orders, left_on='id', right_on='cust_id', how='outer')
result = merged[['first_name', 'last_name', 'city', 'order_details']].sort_values(['first_name', 'order_details'], ascending=[1,0])