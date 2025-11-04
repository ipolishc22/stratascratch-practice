# 10560 olympic team switches
import pandas as pd

olympic_games_athletes.head()

df = olympic_games_athletes.copy()
df['team_count'] = df.groupby(['name'])['team'].transform('nunique')
df[df['team_count'] > 1][['name', 'team', 'games', 'sport', 'medal']]