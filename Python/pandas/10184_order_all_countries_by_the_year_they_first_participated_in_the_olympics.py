# 10184 order all countries by the year they first participated in the olympics
import pandas as pd 

olympics_athletes_events.head()

olympics_athletes_events.head()
df = olympics_athletes_events

result = df.groupby(['noc'])['year'].min().to_frame('first_time_year').reset_index().sort_values(['first_time_year', 'noc'])