from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from memory import get_relevant, store_memory
from llm import chat, extract

app = FastAPI()

@app.get("/")
def ui():
    return FileResponse("static/index.html")


@app.post("/chat")
def talk(q: str = Query(..., description="User message")):
    print("Received question:", q)

    # Get relevant memories
    memories = get_relevant(q)
    print("Retrieved memories:", memories)

    # Get AI response
    answer = chat(q, memories)

    # Extract new facts to store
    facts = extract(q, answer)
    print("Extracted facts:", facts)

    for f in facts:
        store_memory(f)

    return {"answer": answer}
