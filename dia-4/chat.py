from langchain_chroma import Chroma
from langchain_ollama import (
        ChatOllama,
        OllamaEmbeddings
)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
import json
import time

MODEL = "qwen3:7b"
TEMPERATURE = 0.5

embeddings = OllamaEmbeddings(model="nomic-embed-text")
store = Chroma(
    collection_name="manuales",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
)



def prompt_con(docs: list, pregunta: str) -> str:
    contexto = "\n\n".join(
        f"[{d.metadata.get('source', '?')} p.{d.metadata.get('page', '?')}]\n{d.page_content}"
        for d in docs
    )
    return f"""Responde la pregunta usando solo el contexto siguiente.
Si la respuesta no está en el contexto, di "No tengo esa información".
Cita la fuente entre corchetes cuando uses un fragmento.

CONTEXTO:
{contexto}

PREGUNTA: {pregunta}

RESPUESTA:"""


MODEL = "qwen3:14b"
TEMPERATURE = 0.2


llm = ChatOllama(model=MODEL, temperature=TEMPERATURE)


def rag_con_logs(pregunta: str) -> str:
    t0 = time.time()
    docs = store.similarity_search(pregunta, k=4)
    print("Docs: ", len(docs))
    respuesta = llm.invoke(prompt_con(docs, pregunta)).content
 
    # Tres campos que valen oro al depurar:
    Path("traces.jsonl").open("a").write(json.dumps({
        "pregunta": pregunta,
        "doc_ids": [d.metadata.get("source") for d in docs],
        "latencia_s": round(time.time() - t0, 2),
    }, ensure_ascii=False) + "\n")
    return respuesta

print(rag_con_logs("Qué obligaciones establece la ley tributaria?"))    
