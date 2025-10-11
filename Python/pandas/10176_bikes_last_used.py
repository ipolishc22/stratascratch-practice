# 10176 Bikes Last Used
import pandas as pd

dc_bikeshare_q1_2012.head()

result = dc_bikeshare_q1_2012.groupby('bike_number')['end_time'].max().to_frame('last_used').reset_index().sort_values('last_used', ascending=False)
result