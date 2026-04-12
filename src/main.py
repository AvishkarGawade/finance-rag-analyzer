from ingestion.load_data import load_data
from processing.clean_data import clean_data
from processing.chunking import create_chunks
from embeddings.embedder import create_vector_store
from retrieval.retriever import retrieve_chunks
from llm.generator import answer_question

def main():
    df = load_data()
    df = clean_data(df)
    chunks = create_chunks(df)
    vectorstore = create_vector_store(chunks)   

    query = "How much did I spend in March"
    # query = "How are you"
    # query = "What are my last 10 transactions"

    response = answer_question(query)
    print("-------------------------------------------")
    print(response)

if __name__ == "__main__":
    main()