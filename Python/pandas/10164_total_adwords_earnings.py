# 10164 total adwords earnings
import pandas as pd

google_adwords_earnings.head()

result = google_adwords_earnings.groupby('business_type')['adwords_earnings'].sum().reset_index()