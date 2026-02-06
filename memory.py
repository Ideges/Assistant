import chromadb
import os

# Ensure data folder exists
os.makedirs("data/chroma", exist_ok=True)

# Initialize Chroma client
db = chromadb.Client(
    settings=chromadb.Settings(
        persist_directory="data/chroma"
    )
)

# Create or get collection
col = db.get_or_create_collection("brain")


def get_relevant(text):
    try:
        r = col.query(query_texts=[text], n_results=8)
        if r["documents"] and len(r["documents"][0]) > 0:
            return r["documents"][0]
        return []
    except Exception as e:
        print("Memory retrieval error:", e)
        return []


def store_memory(text):
    if not text or text.strip() == "":
        return
    try:
        col.add(
            documents=[text],
            ids=[str(abs(hash(text)))]
        )
        print("Stored memory:", text)
    except Exception as e:
        print("Memory store error:", e)
