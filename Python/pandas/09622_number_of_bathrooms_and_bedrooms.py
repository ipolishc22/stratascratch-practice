# 9622 Number of Bathrooms and Bedrooms
import pandas as pd

airbnb_search_details.head()
airbnb_search_details.groupby(["city", "property_type"])[["bathrooms", "bedrooms"]].mean().reset_index().rename(columns={"bathrooms":"n_bathrooms_avg", "bedrooms":"n_bedrooms_avg"})