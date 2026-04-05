import os
import pandas as pd # type: ignore


def total_revenue_by_category(df):
    results = df.groupby("Category")["Revenue"].sum()
    return results

def top_selling_product(df):
    results = df.groupby("Product_Name")["Quantity"].sum().idxmax()
    return results

def monthly_sales_trends(df):
    df["Month"] = df["Date"].dt.month
    results= df.groupby("Month")["Revenue"].sum()
    return results




