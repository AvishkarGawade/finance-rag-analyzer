import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

def get_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(
        persist_directory="vector_db", 
        embedding_function=embeddings
        )
    retriever = vectorstore.as_retriever()

    return retriever

def retrieve_chunks(query):
    retriever = get_retriever()
    response = retriever.invoke(query)
    return response

