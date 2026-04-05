import os
import pandas as pd # type: ignore


def read_data(filepath):
    df = pd.read_csv(filepath)
    return df


def clean_data(df):
    df = df.dropna() 
    df = df.drop_duplicates()
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def process_data(df):
    df["Revenue"] = df["Quantity"] * df["Price"]
    return df

