from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import requests

API_KEY = "VyuJGyw9ejTo66QJLPuD5eRsXVTiR3302URgCmKNzwpnMZN3j48"
headers = {"Authorization": f"Bearer {API_KEY}"}

def fetch_data():
    response = requests.get("https://api.pandascore.co/csgo/teams", headers=headers)
    teams = response.json()
    documents = []
    for team in teams:
        documents.append(f"Time: {team['name']}, Jogadores: {', '.join([p['name'] for p in team['players']])}")
    return documents

def create_faiss_index():
    documents = fetch_data()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(documents, embeddings)
    vectorstore.save_local("faiss_index")
    print("FAISS index created and saved to faiss_index")

if __name__ == "__main__":
    create_faiss_index()