# 9924 Email Preference Missing
import pandas as pd

library_usage.head()
# notice_preference_definition
# provided_email_address
result = library_usage[(library_usage['notice_preference_definition'] == 'email') & (library_usage['provided_email_address'] == False) & (library_usage['circulation_active_year'] == 2016)][['home_library_code']].drop_duplicates()