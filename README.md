## Agentic RAG System

This project implements an **agentic Retrieval-Augmented Generation (RAG)** pipeline designed to produce **grounded, self-evaluated answers** rather than free-form LLM responses.

Instead of answering questions in a single pass, the system treats question answering as a **multi-step reasoning process**:
1. Retrieve relevant documents from a vector database
2. Grade the retrieved evidence for relevance and sufficiency
3. Escalate to web search when local knowledge is insufficient
4. Generate an answer constrained by supporting evidence
5. Evaluate the final answer for usefulness and factual support before returning it


## Agentic RAG

Agentic RAG is an experiment and small framework for building agentic, evidence-grounded Retrieval-Augmented Generation (RAG) pipelines. The system treats question answering as a multi-step, agentic process that retrieves information, validates evidence, optionally escalates to web search, and generates answers constrained by verified supporting material.

### Overview

The goal of Agentic RAG is to reduce hallucination and produce answers that are accompanied by explicit evidence and automatic self-evaluation. The core orchestration is implemented as a graph of modular nodes and chains which allows dynamic routing, retries, and quality checks during generation.

Key ideas:
- Retrieve documents from a vector store (Chroma) using dense embeddings.
- Grade retrieved evidence for relevance and sufficiency before generating.
- Use evidence-constrained generation to force the model to cite supporting sources.
- Apply graders (retrieval grader, hallucination grader, answer grader) to validate outputs.

### Features

- Vector-based retrieval with persistent Chroma DB
- Agentic control flow: conditional routing, retries, and halting
- Modular chains and nodes implemented with LangChain primitives
- Document/answer grading and hallucination detection
- Pluggable web-search escalation when local data is insufficient

### Installation

Prerequisites:
- Python 3.11+
- (recommended) a virtual environment tool: `python -m venv`, `poetry`, or `uv`

Install dependencies via Poetry (project contains `pyproject.toml`):

```bash
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install
```

Or install with pip after exporting a `requirements.txt` from the project metadata.

### Quick Start

1. Create and activate a virtual environment (see Install).
2. Create a `.env` file with any required API keys (OpenAI, other LLM providers).
3. Ingest documents into the vector store (if you have local data):

```bash
python ingestion.py
```

4. Run the example runner / orchestrator:

```bash
python main.py
```

Notes:
- The repo includes a local Chroma DB folder (`.chroma`). Avoid committing large vector databases — add `.chroma/` to `.gitignore` (already present).
- Keep secrets out of source control; use `.env` for credentials and add `.env` to `.gitignore`.

### Programmatic Usage (example)

The repository exposes modular graph and chain components which can be imported and composed programmatically. Example (high-level):

```python
from graph.graph import Graph
from graph.chains.generation import GenerationChain

# create/compose graph programmatically, then run
g = Graph()
# configure nodes/chains in code or via helper functions
g.run()
```

(See `graph/` for concrete chain and node implementations.)

### Testing

Run the test suite with `pytest`:

```bash
pytest -q
```

### Output & Formats

This project doesn't currently define a CLI with multiple output formats, but `main.py` prints or logs results; you can adapt nodes to return structured JSON or other formats for machine consumption.

### Documentation & Next Steps

- `graph/` contains the primary implementation: `graph.py`, `state.py`, `chains/`, and `nodes/`.
- I can add a dedicated `docs/agentic-rag.md` modeled after the MCP Scanner README with more examples, or add a lightweight CLI wrapper that supports multiple output formats similar to MCP Scanner.

### License

If you want this project published with a permissive license, I can add an `LICENSE` file (e.g., MIT) and push it.
