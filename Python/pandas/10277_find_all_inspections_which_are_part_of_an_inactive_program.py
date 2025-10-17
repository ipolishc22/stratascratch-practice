# 10277 Find all inspections which are part of an inactive program
import pandas as pd

los_angeles_restaurant_health_inspections.head()
los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections['program_status'].isin(['INACTIVE'])]