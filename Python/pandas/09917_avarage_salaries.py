# 9917 Average Salaries 
import pandas as pd

employee.head()
employee['average_salary'] = employee.groupby(['department'])['salary'].transform('mean')
result = employee[['department', 'first_name', 'salary', 'average_salary']]
result = result.sort_values(by='department')