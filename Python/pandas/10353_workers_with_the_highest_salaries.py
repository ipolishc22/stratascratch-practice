# 10353 Workers With the Highest Salaries
import pandas as pd

worker.head()
title.head()

merged = pd.merge(worker, title, left_on="worker_id", right_on="worker_ref_id")
max_salary = merged[merged["salary"] == merged["salary"].max()][["worker_title"]]
