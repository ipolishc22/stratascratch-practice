# 2056 Number of Shipments per Month
import pandas as pd

amazon_shipment['year_month'] = pd.to_datetime(amazon_shipment.shipment_date).dt.to_period('M')
amazon_shipment['unique_key'] = amazon_shipment['shipment_id'].astype(str) + '_' + amazon_shipment['sub_id'].astype(str)
result = amazon_shipment.groupby('year_month')['unique_key'].nunique().to_frame('count').reset_index()
result.head()