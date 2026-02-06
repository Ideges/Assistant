from fastapi import FastAPI
from fastapi.responses import FileResponse
from memory import get_relevant, store_memory
from llm import chat, extract

app = FastAPI()

@app.get("/")
def ui():
    return FileResponse("static/index.html")


@app.post("/chat")
def talk(q: str):

    # 1) recall relevant memories
    memories = get_relevant(q)

    # 2) ask LLM
    answer = chat(q, memories)

    # 3) extract new facts to store
    facts = extract(q, answer)

    for f in facts:
        if f.strip():
            store_memory(f)

    return {"answer": answer}
