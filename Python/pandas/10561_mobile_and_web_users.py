# 10561 mobile and web users
import pandas as pd

mobile_logs.head()
web_logs.head()

logs = pd.concat([
    mobile_logs[['user_id', 'log_date']], 
    web_logs[['user_id', 'log_date']]
])
    
result = logs.groupby(['log_date'])['user_id'].nunique().reset_index(name='n_users')