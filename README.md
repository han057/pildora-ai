# Píldora AI — Fundación SPLAI

Currículo práctico para construir aplicaciones con **LLMs locales** de forma
incremental a lo largo de varios días (`dia-1` … `dia-5`), más un proyecto
integrador (`proyecto_base/`) y una demo con Docker (`docker_demo/`).

Todo corre contra un **servidor Ollama local** (`http://localhost:11434`); no se
necesitan claves de API ni servicios en la nube.

> Cada día es un conjunto de scripts independientes. Los conceptos se acumulan,
> pero el código no: para entender un día, lee sus scripts.

---

## Requisitos previos

| Herramienta | Para qué | Comprobar |
|-------------|----------|-----------|
| **Python 3.14** | Lenguaje del proyecto | `python --version` |
| **Ollama** | Servidor de LLMs locales | `ollama --version` |
| **git** | Clonar el repositorio | `git --version` |

> [!NOTE]
> El proyecto usa Python **3.14** (ver `.python-version`). 

## Paso a paso

### 1. Clonar el repositorio

```bash
git clone <URL-del-repositorio> pildora-ai
cd pildora-ai
```

### 2. Crear y activar el entorno virtual

```bash
# Linux / macOS
python -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Mientras el entorno esté activo, el prompt mostrará `(.venv)`. Para salir más
tarde, usa `deactivate`.

### 3. Instalar dependencias

Con el entorno activado, instala las dependencias declaradas en
`requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

A partir de aquí, con el entorno activo, los scripts se ejecutan con
`python <script>`.

### 4. Instalar Ollama

Ollama sirve los modelos de lenguaje en local.

```bash
# Linux
curl -fsSL https://ollama.com/install.sh | sh

# macOS  → descargar la app desde https://ollama.com/download
# Windows → descargar el instalador desde https://ollama.com/download
```

Arranca el servidor (en Linux suele quedar como servicio; si no, ejecuta):

```bash
ollama serve
```

Comprueba que responde en `http://localhost:11434`:

```bash
curl http://localhost:11434/api/tags
```

### 5. Descargar los modelos

Los scripts referencian el modelo mediante constantes `MODEL` / `LLM_MODEL` y
**varían por script**. Los embeddings siempre usan `nomic-embed-text`.

Descarga los modelos que vayas a usar con `ollama pull`:

```bash
# Embeddings (necesario para todo lo de RAG: dia-3, dia-4, dia-5, proyecto_base)
ollama pull nomic-embed-text

# Modelos de chat usados en los distintos scripts
ollama pull gemma3:4b      # proyecto_base y docker_demo
ollama pull qwen3:8b       # varios scripts dia-1…dia-5

# Modelos más grandes (solo si tu hardware los soporta y un script los pide)
ollama pull qwen3:7b
ollama pull qwen3:14b
ollama pull qwen3:30b
```

Verifica qué tienes descargado:

```bash
ollama list
```

> [!IMPORTANT]
> Algunos scripts apuntan a modelos que quizá no tengas descargados. Si un script
> falla por modelo no encontrado, edita su constante `MODEL` / `LLM_MODEL` para
> usar uno que sí tengas (p. ej. `qwen3:8b` o `gemma3:4b`) en lugar de asumir que
> existe.

---

## Ejecutar los scripts — el directorio de trabajo importa

Los scripts usan **rutas relativas** y el directorio correcto **no es siempre el
mismo**:

> Recuerda tener el entorno virtual activado (`source .venv/bin/activate`).

- **dia-1** — scripts autocontenidos, se ejecutan desde cualquier sitio:
  ```bash
  python dia-1/<script>.py
  ```

- **dia-2** — se ejecuta **desde dentro de `dia-2/`** (hace `from tools import ...`):
  ```bash
  cd dia-2 && python agente_multitool.py
  ```

- **dia-3 / dia-4** — se ejecutan **desde la raíz del repo** (abren ficheros como
  `manual.pdf`, `Preguntas_frecuentes_FAQ.md`, `./docs/`, `./chroma_db`):
  ```bash
  python dia-3/rag_minimo.py
  python dia-4/chroma_persistente.py
  ```

- **dia-5** — grafo de LangGraph con enrutado y arnés de pruebas:
  ```bash
  python dia-5/langgraph_example.py
  ```

---

## Proyecto integrador (`proyecto_base/`)

Chatbot de soporte de Python con recepción y escalado en niveles (FastAPI +
LangGraph + Chroma). Desde la **raíz del repo**:

```bash
uvicorn proyecto_base.app.main:app --reload
```

- UI de chat: http://localhost:8000/
- API / Swagger: http://localhost:8000/docs

Usa `gemma3:4b` y `nomic-embed-text` (ver `proyecto_base/app/config.py`).
Más detalles en [`proyecto_base/README.md`](proyecto_base/README.md).

---

## Demo con Docker (`docker_demo/`)

Levanta FastAPI + Ollama en contenedores. Requiere **Docker** y **Docker Compose**:

```bash
cd docker_demo
docker compose up -d
docker compose exec ollama ollama pull gemma3:4b   # descargar el modelo dentro del contenedor
```

Luego abre, por ejemplo: `http://localhost:8000/chat?pregunta=¿Quién eres?`

---

## Notas y estado compartido

- **`./chroma_db/`** — almacén Chroma persistido en disco, compartido por
  dia-3/4/5 en colecciones distintas. Está en `.gitignore`. Reindexar es seguro
  (usa IDs deterministas), pero cambiar el *chunking* o los metadatos sin limpiar
  el store puede dejar vectores obsoletos.
- **`traces.jsonl`** — los scripts de RAG le hacen *append* (pregunta, fuentes,
  latencia) en cada ejecución; crece con el uso.
- **Idioma** — código, comentarios y prompts están en **español**.
- **Formato** — el formateador configurado es **black**.

---

## Resolución de problemas

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| `Connection refused` a `:11434` | Ollama no está corriendo | `ollama serve` |
| `model "..." not found` | Modelo no descargado | `ollama pull <modelo>` o cambia la constante del script |
| `FileNotFoundError` (PDF/MD) | Directorio de trabajo incorrecto | Ejecuta dia-3/4 desde la raíz; dia-2 desde `dia-2/` |
| Dependencia ausente | Entorno no activado o sin instalar | Activa `.venv` y `pip install -r requirements.txt` |
```
