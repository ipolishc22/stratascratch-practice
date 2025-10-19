# 9972 Captain Base Pay 
import pandas as pd

sf_public_salaries.head()
result = sf_public_salaries[(sf_public_salaries['jobtitle'].str.contains('CAPTAIN', case=False)) & (sf_public_salaries['jobtitle'].str.contains('POLICE', case = False))][['employeename', 'basepay']]
result