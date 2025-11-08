# 10167 total number of housing units
import pandas as pd

housing_units_completed_us.head()

result = housing_units_completed_us.groupby('year')[['south', 'west', 'midwest', 'northeast']].sum().reset_index()
result['total'] = result['south'] + result['west'] + result['midwest'] + result['northeast']
result = result[['year', 'total']]
print(result)