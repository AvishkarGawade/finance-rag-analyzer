from ingestion.load_data import load_data
from processing.clean_data import clean_data
from processing.chunking import create_chunks
from embeddings.embedder import create_vector_store

def main():
    df = load_data()
    df = clean_data(df)
    chunks = create_chunks(df)
    vectorstore = create_vector_store(chunks)   

if __name__ == "__main__":
    main()