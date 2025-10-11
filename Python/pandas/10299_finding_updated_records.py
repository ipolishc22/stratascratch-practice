# 10299 finding Updated Records
import pandas as pd

ms_employee_salary.head()

ms_employee_salary = ms_employee_salary.copy()
ms_employee_salary['rn'] = ms_employee_salary.sort_values(['salary', 'department_id'], ascending=[False, False]).groupby('id').cumcount() + 1

result = ms_employee_salary[ms_employee_salary['rn'] == 1].drop(columns='rn').sort_values('id').reset_index(drop=True)
result