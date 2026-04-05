from ingestion.load_data import load_data
from processing.clean_data import clean_data

def main():
    df = load_data()
    df = clean_data(df)


if __name__ == "__main__":
    main()