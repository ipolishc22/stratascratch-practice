# 10238 find the top ranked songs of the past 20 years
import pandas as pd

billboard_top_100_year_end.head()

df = billboard_top_100_year_end.copy()
df = df[(df['year_rank'] == 1) & (df['year']>=2005)]['song_name'].drop_duplicates().reset_index(drop=True)