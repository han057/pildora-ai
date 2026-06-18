from langchain_ollama import OllamaEmbeddings
import numpy as np

emb = OllamaEmbeddings(model="nomic-embed-text")

textos = [
    "El gato duerme en el sofá",
    "Un felino descansa en el mueble",
    "Python es un lenguaje de programación",
]

vectores = emb.embed_documents(textos)
print(f"Cada vector tiene {len(vectores[0])} dimensiones")


def cos_sim(a, b):
    a, b = np.array(a), np.array(b)
    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))


print(f"gato/felino: {cos_sim(vectores[0], vectores[1]):.3f}")
print(f"gato/python: {cos_sim(vectores[0], vectores[2]):.3f}")
