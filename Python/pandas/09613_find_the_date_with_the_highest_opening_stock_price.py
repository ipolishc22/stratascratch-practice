# 9613 find the date with the highest opening stock price
import pandas as pd 
import numpy as np 
import datetime, time 

aapl_historical_stock_price.head()

df = aapl_historical_stock_price.copy()
# copy the dataframe for easier work
df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
# switch the date column from datetime to string format
result = df[df['open'] == df['open'].max()][['date']]
result