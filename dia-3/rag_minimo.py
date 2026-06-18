from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
 
# 1. Cargar PDF
docs = PyPDFLoader("manual.pdf").load()
 
# 2. Trocear en chunks de ~800 caracteres
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(docs)
 
# 3. Embeddings + vectorstore persistente
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_documents(
    chunks, embeddings,
    persist_directory="./chroma_db")


llm = ChatOllama(model="qwen3:8b", temperature=0)

def rag(pregunta: str) -> str:
    docs_relevantes = vectorstore.similarity_search(pregunta, k=4)
    contexto = "\n\n".join(d.page_content for d in docs_relevantes)
    prompt = f"""Responde la pregunta usando solo el contexto siguiente.
Si la respuesta no está en el contexto, di "No tengo esa información".
 
CONTEXTO:
{contexto}
 
PREGUNTA: {pregunta}
 
RESPUESTA:"""
    return llm.invoke(prompt).content

print(rag("¿Qué tema trata este curso?"))
