# 10128 Abigail Breslin Nominations
import pandas as pd

oscar_nominees.head()

# my solution
oscar_nominees[oscar_nominees['nominee'].isin(['Abigail Breslin'])].count().unique()

# provided sample solution
nominee = oscar_nominees[oscar_nominees['nominee'] == 'Abigail Breslin']
result = nominee.movie.nunique()