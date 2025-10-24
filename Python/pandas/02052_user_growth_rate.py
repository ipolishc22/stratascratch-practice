# 2052 User Growth Rate
import pandas as pd

sf_events.head()

sf_events['record_date'] = pd.to_datetime(sf_events['record_date'], format='%Y-%m-%d')
dec_2020 = sf_events[(sf_events['record_date'].dt.year == 2020) & (sf_events['record_date'].dt.month == 12)].groupby('account_id')['user_id'].nunique().to_frame('dec_count').reset_index()
jan_2021 = sf_events[(sf_events['record_date'].dt.year == 2021) & (sf_events['record_date'].dt.month == 1)].groupby('account_id')['user_id'].nunique().to_frame('jan_count').reset_index()
merged = jan_2021.merge(dec_2020, on='account_id')
merged['ratio'] = merged['jan_count'] / merged['dec_count']

result = merged[['account_id', 'ratio']]
result