# 10166 reviews of hotel arena 
import pandas as pd

hotel_reviews.head()

arena = hotel_reviews[hotel_reviews['hotel_name'] == 'Hotel Arena']
result = arena.groupby(['hotel_name', 'reviewer_score']).size().reset_index(name='count')