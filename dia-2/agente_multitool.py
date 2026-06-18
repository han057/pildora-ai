from langchain_core import messages
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

from tools import calculate, get_current_time, convert_currency

MODEL = "qwen3:30b"
TEMPERATURE = 0.9


llm = ChatOllama(model=MODEL, temperature=TEMPERATURE)

agent = create_agent(
    llm,
    tools=[calculate, get_current_time, convert_currency],
)

queries = [
    "¿Cuántos euros son 250 dólares?",
    "¿Cuánto es 47 * 83?",
    "Dime la hora y luego suma 17 + 25.",
]
for q in queries:
    print(f"\n>>> {q}")
    message = HumanMessage(q)
    result = agent.invoke({"messages": [message]})
    print(result["messages"][-1].content)
