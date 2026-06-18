import requests

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "qwen3:8b",
        "messages": [{"role": "user", "content": "Explica RAG en una frase."}],
        "stream": False,
    },
)

print(response.json()["message"]["content"])
