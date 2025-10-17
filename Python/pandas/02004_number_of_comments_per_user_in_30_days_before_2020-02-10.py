# 2004 Number of comments per user in 30 days before 2020-02-10
import pandas as pd
from datetime import timedelta

fb_comments_count.head()
fb_comments_count[(fb_comments_count['created_at'] >= pd.to_datetime('2020-02-10') - timedelta(days=30)) & 
                  (fb_comments_count['created_at'] <= pd.to_datetime('2020-02-10'))].groupby('user_id')['number_of_comments'].sum().reset_index()