# 2107 primary key violation
import pandas as pd 

dim_customer.head() 

grouped = dim_customer.groupby(['cust_id']).size().rename('n_occurences').reset_index()
result = grouped[grouped['n_occurences'] > 1]
result