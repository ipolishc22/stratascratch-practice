# 2091 latest login date
import pandas as pd 

player_logins.head()

result = players_logins.groupby(['player_id'])['login_date'].max().reset_index()
result