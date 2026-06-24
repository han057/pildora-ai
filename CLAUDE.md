# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A hands-on teaching curriculum ("píldora AI") for Fundación SPLAI that builds local-LLM
applications incrementally across five days (`dia-1` … `dia-5`). Each day is a set of
standalone scripts, not an importable package — there is no shared library, no entry point
that ties them together, and `main.py` is just a stub. Read a day's scripts to understand
that day; concepts compound across days but code does not.

Everything runs against a **local Ollama server** (`http://localhost:11434`) — no cloud API
keys. Ollama must be running and the referenced models pulled before any script works.

## Progression (the architecture)

- **dia-1** — Three ways to call an LLM: raw HTTP (`requests`), LangChain wrapper
  (`ChatOllama`), and a first tool-calling agent via `create_agent`.
- **dia-2** — Multi-tool agent. Tools live in `tools.py`, the agent in `agente_multitool.py`.
- **dia-3** — Embeddings + minimal RAG: `OllamaEmbeddings`, cosine similarity, then a full
  PDF → chunk → Chroma → retrieve → answer pipeline.
- **dia-4** — Production-leaning RAG: persistent Chroma collections, deterministic chunk IDs
  for idempotent re-indexing, enriched metadata + source citations, JSONL tracing, and a
  comparison of chunking strategies.
- **dia-5** — `langgraph_example.py`: a `StateGraph` that classifies a query and routes it
  (técnica → RAG pipeline, facturación, general), plus a `TestHarness` with pass/fail
  assertions and latency metrics.

## Running scripts — working directory matters

Scripts use **relative paths**, and the correct working directory is inconsistent:

- **dia-2** must run from inside `dia-2/` (it does `from tools import ...`):
  ```bash
  cd dia-2 && uv run python agente_multitool.py
  ```
- **dia-3 / dia-4** must run from the **repo root** — they open root-level files like
  `manual.pdf`, `Preguntas_frecuentes_FAQ.md`, `./docs/`, and `./chroma_db`:
  ```bash
  uv run python dia-3/rag_minimo.py
  uv run python dia-4/chroma_persistente.py
  ```
- Other scripts are self-contained and run from anywhere.

When adding or moving a script, keep these path assumptions in mind — a script that reads a
data file will break if launched from the wrong directory.

## Environment

- Python **3.14**, managed with **uv** (`uv.lock` is the source of truth; `requirements.txt`
  mirrors `pyproject.toml`). Use `uv sync` to install and `uv run python <script>` to run.
- Models are hardcoded per-script via `MODEL` / `LLM_MODEL` constants and vary
  (`qwen3:8b`, `qwen3:14b`, `qwen3:30b`, etc.). Some scripts reference models that may not be
  pulled locally — check `ollama list` and adjust the constant rather than assuming a model
  exists. Embeddings always use `nomic-embed-text`.
- Formatting: **black** is the configured formatter.

## Shared state to be careful with

- `./chroma_db/` is a persisted Chroma store on disk, shared across dia-3/4/5 but split into
  different collections (`manuales`, `soporte_tecnico`, default). It is gitignored. Re-running
  indexing scripts is safe because they use deterministic IDs (`f"{source}_{i}"`), but
  changing chunking or metadata without clearing the store can leave stale vectors.
- `traces.jsonl` is appended to by the RAG scripts (question, doc sources, latency) for
  debugging — it grows on every run.

## Conventions

- Code, comments, prompts, and docstrings are in **Spanish**. Match this when editing.
- RAG prompts follow a fixed pattern: answer only from provided context, say "No tengo esa
  información" when absent, cite sources in brackets. Reuse this phrasing for consistency.
