import pandas as pd 

def load_data(file_path='data/raw/transactions.csv'):
    return pd.read_csv(file_path)

def validate_data(df):
    print("columns -> :  ",df.columns)
    print(df.isna().sum())

    transactions = len(df)
    income = df[df["amount"] > 0 ]["amount"].sum()
    expense = df[df["amount"] < 0 ]["amount"].sum()

    print(f"\nTotal transactions : {transactions}")
    print(f"\nIncome : ₹{income}")
    print(f"\nExpense : ₹{abs(expense)}")


if __name__ == "main":
    df = load_data(file_path)
    print(df.head())
    validate_data(df)

