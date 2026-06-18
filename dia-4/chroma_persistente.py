from langchain_chroma import Chroma
from langchain_ollama import (
        OllamaEmbeddings,
        ChatOllama
)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
import json
import time
 
embeddings = OllamaEmbeddings(model="nomic-embed-text")
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
 
# Conectar (o crear) un store persistente
store = Chroma(
    collection_name="manuales",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
)
 
# Indexar varios PDFs con metadatos enriquecidos
for pdf in Path("./docs").glob("*.pdf"):
    print(f"Indexando {pdf}")
    loader = PyPDFLoader(str(pdf))
    pages = loader.load()
    chunks = splitter.split_documents(pages)
    # Añadir metadatos útiles
    print(f"Añadiendo metadatos a {pdf}")
    for c in chunks:
        c.metadata["source"] = pdf.name
        c.metadata["categoria"] = "manual" if "manual" in pdf.name else "FAQ"
        c.metadata["año"] = 2025  # extraer de algún sitio
    # Usar ids deterministas para poder reindexar sin duplicar
    ids = [f"{pdf.name}_{i}" for i in range(len(chunks))]
    store.add_documents(chunks, ids=ids)
 
# Búsqueda con filtro
"""resultados = store.similarity_search(
    "Qué obligaciones establece la ley tributaria?",
    k=4,
    filter={"categoria": "FAQ"},
)
for r in resultados:
    print(f"[{r.metadata['source']} p.{r.metadata.get('page', '?')}]")
    print(r.page_content[:200])
    print()
"""


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


MODEL = "qwen3:30b"
TEMPERATURE = 0.9


llm = ChatOllama(model=MODEL, temperature=TEMPERATURE)


def rag_con_logs(pregunta: str) -> str:
    t0 = time.time()
    docs = store.similarity_search(pregunta, k=4)
    respuesta = llm.invoke(prompt_con(docs, pregunta)).content
 
    # Tres campos que valen oro al depurar:
    Path("traces.jsonl").open("a").write(json.dumps({
        "pregunta": pregunta,
        "doc_ids": [d.metadata.get("source") for d in docs],
        "latencia_s": round(time.time() - t0, 2),
    }, ensure_ascii=False) + "\n")
    return respuesta

print(rag_con_logs("Qué obligaciones establece la ley tributaria?"))
