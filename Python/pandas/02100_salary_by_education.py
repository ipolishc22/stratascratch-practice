# 2100 salary by education
import pandas as pd

google_salaried.head()

result = google_salaries.groupby(['education'])['salary'].mean().reset_index(name='average_salary')
result