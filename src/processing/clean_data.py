import pandas as pd
import numpy as np

def clean_data(df):
    df["category"] = df["category"].fillna("Other")
    df["category"] = df["category"].str.title()
    df["description"] = df["description"].str.strip().str.lower()    
    df["amount"] = pd.to_numeric(df["amount"])
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "amount"])

    df["month"] = df["date"].dt.to_period("M").astype(str)
    df["day_of_week"] = df["date"].dt.day_name()
    
    df = df.drop_duplicates()
    df["type"] = np.where(df["amount"] > 0, "income", "expense")

    df.to_csv("data/processed/cleaned_transactions.csv", index=False)
