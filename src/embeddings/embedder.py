import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()
hf_token = os.getenv("HF_TOKEN")

def create_vector_store(chunks):
    db_name = "vector_db"
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    documents = [Document(page_content=chunk) for chunk in chunks]

    if os.path.exists(db_name):
        vectorstore = Chroma(persist_directory=db_name, embedding_function=embeddings)
    else:
        vectorstore = Chroma.from_documents(
            documents=documents, 
            embedding=embeddings, 
            persist_directory=db_name)
        
    return vectorstore
