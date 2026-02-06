import chromadb

db = chromadb.Client(
    settings=chromadb.Settings(
        persist_directory="data/chroma"
    )
)

col = db.get_or_create_collection("brain")


def get_relevant(text):
    r = col.query(query_texts=[text], n_results=8)
    return r["documents"][0] if r["documents"] else []


def store_memory(text):
    col.add(
        documents=[text],
        ids=[str(abs(hash(text)))]
    )
