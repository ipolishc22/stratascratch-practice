# Find all posts which were reacted to with a heart
import pandas as pd

facebook_reactions.head()

heart = facebook_reactions[facebook_reactions['reaction'] == 'heart'][['post_id']]
result = pd.merge(heart, facebook_posts, on='post_id').drop_duplicates(subset='post_id')
result