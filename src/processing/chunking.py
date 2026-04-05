import pandas as pd

def create_chunks(df):
    df["date"] = pd.to_datetime(df["date"])

    chunks = []

    for _, row in df.iterrows():

        formatted_date = row["date"].strftime("%d %B %Y")
        amount = abs(row["amount"])
        description = row["description"]
        category = row["category"]
        transaction_type = "received" if row["type"] == "income" else "spent"

        chunk = f"On {formatted_date}, {transaction_type} ₹{amount} for {description} under {category} category."
        chunks.append(chunk)

    return chunks

df = pd.read_csv('data/processed/cleaned_transactions.csv')

if __name__ == "__main__":
    chunks = create_chunks(df)