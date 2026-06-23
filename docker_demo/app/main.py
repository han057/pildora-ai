import os
from fastapi import FastAPI
from langchain_ollama import ChatOllama

# Obtener la URL de Ollama desde variable de entorno
ollama_base_url = os.getenv("OLLAMA_API_BASE_URL", "http://localhost:11434")

llm = ChatOllama(
    model="gemma3:4b", 
    temperature=0,
    base_url=ollama_base_url
)
app = FastAPI()

@app.get("/chat")
def read_chat(pregunta: str):
    response = llm.invoke(pregunta)
    return {"message": response}

items = {
    "1": {"name": "Item 1", "price": 10.0},
    "2": {"name": "Item 2", "price": 20.0},
}

@app.get("/")
def read_root():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: str):
    return items.get(
        item_id, 
        {"message": "Item not found"}
    )

