# 9915 Highest Cost Orders
import pandas as pd

orders["order_date"] = pd.to_datetime(orders["order_date"])
orders = orders[orders["order_date"].between("2019-02-01", "2019-05-01")]

daily_totals = (
    orders.groupby(["cust_id", "order_date"])["total_order_cost"]
    .sum()
    .reset_index()
    )
    

daily_max = (
    daily_totals.groupby("order_date")["total_order_cost"]
    .transform("max")
    )

top_daily = daily_totals[daily_totals["total_order_cost"] == daily_max]

result = top_daily.merge(customers, left_on="cust_id", right_on="id")
result["order_date"] = result["order_date"].dt.strftime("%Y-%m-%d")

result = result[["first_name", "order_date", "total_order_cost"]].rename(columns = {"total_order_cost" : "max_cost"})

result