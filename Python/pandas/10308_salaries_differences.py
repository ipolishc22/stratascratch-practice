# 10308 Salaries Difference
import pandas as pd

db_employee.head()
db_dept.head()

merged = pd.merge(db_employee, db_dept, left_on="department_id", right_on="id")
filtered = merged[merged['department'].isin(["engineering", "marketing"])]
grouped = filtered.groupby(['department']).max()
grouped['salary_difference'] = grouped['salary'] - grouped['salary'].shift(1)
grouped['salary_difference'].dropna()
