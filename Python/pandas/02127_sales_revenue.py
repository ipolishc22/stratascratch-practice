# 2127 sales revenue 
import pandas as pd  

amazon_sales.head()

result = amazon_sales[amazon_sales['order_date'].dt.year == 2021]['order_total'].sum()
df = pd.DataFrame({'REVENUE' : [result]})
df
