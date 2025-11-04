# 10559 available seat pairs
import pandas as pd 

theater_availability.head()

df = pd.merge(theater_availability, theater_seatmap, on='seat_number')
df = df.merge(theater_availability, 
    left_on='seat_right',
    right_on='seat_number',
    suffixes=('', '_right'))
result = df[(df['is_available'] == 1) &
    (df['is_available_right'] == 1) &
    (df['seat_right'].notna())][['seat_number', 'seat_right']].rename(
        columns={'seat_number': 'seat', 'seat_right': 'adj_seat'})