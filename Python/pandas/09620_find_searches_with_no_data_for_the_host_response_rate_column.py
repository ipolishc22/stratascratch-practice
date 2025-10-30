# 9620 find searches with no data for the host_response_rate column
import pandas as pd 

airbnb_search_details.head()

airbnb_search_details[airbnb_search_details['host_response_rate'].isnull()]