from ingestion.load_data import load_data
from processing.clean_data import clean_data
from processing.chunking import create_chunks

def main():
    df = load_data()
    df = clean_data(df)
    chunks = create_chunks(df)
    print(f"\n{chunks[:]}")


if __name__ == "__main__":
    main()