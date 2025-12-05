# 10160 rank guests based on their ages
import pandas as pd

airbnb_guests.head()

airbnb_guests['rank'] = airbnb_guests['age'].rank(method='min', ascending=False)
result = airbnb_guests[['guest_id', 'rank']].sort_values('rank', ascending=True)