# 2049 total order per status per service
import pandas as pd 

uber_orders.head()

grouped = uber_orders.groupby(['status_of_order', 'service_name'])['number_of_orders'].sum().reset_index(name='order_sum')
grouped

# in this case .reset_index() is used to create a new column from the sum() of grouped orders