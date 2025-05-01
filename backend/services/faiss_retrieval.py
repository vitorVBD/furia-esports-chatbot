from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
import os

def initialize_faiss():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    index_path = os.path.abspath("faiss_index")  # Caminho absoluto para o índice
    print(f"Loading FAISS index from {index_path}")
    vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    return vectorstore

def initialize_llm():
    return OllamaLLM(model="mistral")

def initialize_retrieval_qa():
    vectorstore = initialize_faiss()
    llm = initialize_llm()
    retriever = vectorstore.as_retriever()
    
    # Cria a cadeia de recuperação usando RetrievalQA
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")
    return qa_chain