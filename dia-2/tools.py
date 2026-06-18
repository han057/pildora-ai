from langchain_core.tools import tool
from datetime import datetime
import requests


@tool
def calculate(expression: str) -> str:
    """Evalúa una expressión aritmética simple. Usar para sumas, restas,
    multiplicaciones, divisiones"""
    try:
        print(f"LLamando calculate con {expression}")
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Resultado: {result}"
    except Exception as e:
        return f"Error al calcular: {e}"


@tool
def get_current_time() -> str:
    """Devuelve la fecha y hora actual en formato ISO 8601."""
    print("LLamando get_current_time")
    return datetime.now().isoformat()


@tool
def convert_currency(amount: float, from_curr: str, to_curr: str) -> str:
    """Convierte un importe entre dos divisas usando tipos de cambio actuales.
    from_curr y to_curr son códigos ISO de 3 letras: EUR, USD, JPY, GBP."""
    print("Llamando convert_currency")
    try:
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_curr}&to={to_curr}"
        r = requests.get(url, timeout=5).json()
        return f"{amount} {from_curr} = {r['rates'][to_curr]} {to_curr}"
    except Exception as e:
        return f"Error en la conversión: {e}"
