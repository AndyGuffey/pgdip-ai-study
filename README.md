# PGDip Study Code — Retrieval-Augmented Generation (RAG)

Running collection of study scripts exploring vector search, embeddings, and
Retrieval-Augmented Generation (RAG), roughly ordered by week/day as covered
in the course (`w2_d4`, `w3_d1`, `w3_d2`, `w3_d3`, ...).

## Topics by file

### Chunking & embeddings
- **[d3_chunk_demo.py](d3_chunk_demo.py)** — Standalone demo of the first half
  of a RAG pipeline: word-based chunking with overlap, embedding chunks with
  `sentence-transformers`, and cosine-similarity search over the resulting
  vectors. No vector database or LLM involved — good for seeing chunking and
  semantic search in isolation.

### Vector databases
- **[w2_d4_vector_db_example3.py](w2_d4_vector_db_example3.py)** — Using
  ChromaDB as a vector store: embedding + storing documents with rich
  metadata, querying with relevance scoring, filtering results by an
  access-control field (`sensitivity`), and sharding a collection across
  multiple ChromaDB collections for scale.

### RAG basics (RAG 1.0)
- **[w3_d1_rag_example_1.py](w3_d1_rag_example_1.py)** — Minimal RAG example:
  embed a few sentences with `HuggingFaceEmbeddings`, store them in FAISS,
  and retrieve the top matches for a query. Retrieval only, no generation.
- **[w3_d1_rag_demo.py](w3_d1_rag_demo.py)** — Full end-to-end RAG pipeline:
  document chunking (`RecursiveCharacterTextSplitter`) → embeddings → FAISS
  vector store → retriever → OpenAI LLM (`gpt-4o-mini`) → generated,
  source-traceable answer. Requires an OpenAI API key.

### Hybrid retrieval (RAG 2.0)
- **[w3_d2_rag2_demo.py](w3_d2_rag2_demo.py)** — Combines sparse keyword
  search (BM25) with dense vector search (FAISS) into a simple hybrid
  retriever, compares results from each method side by side, then feeds the
  merged context to an OpenAI LLM for answer generation. Requires an OpenAI
  API key.

### Reranking & graph retrieval (RAG 3.0)
- **[w3_d3_rag3_reranking_ex.py](w3_d3_rag3_reranking_ex.py)** — Smallest
  possible reranking example: score a fixed list of retrieved documents
  against a query using a `CrossEncoder` and print them in relevance order.
- **[w3_d3_rag3_example](w3_d3_rag3_example)** — Builds a document
  similarity graph with `networkx` (edges added when cosine similarity
  exceeds a threshold) and visualizes it with `matplotlib`.
- **[w3_d3_rag3_simple_rerank.py](w3_d3_rag3_simple_rerank.py)** — Puts it
  all together: a `SimpleRAG3` class that retrieves candidates via
  knowledge-graph traversal (embeddings + manually defined document
  connections), reranks them with a `CrossEncoder`, assembles a context
  string, and renders the knowledge graph with the retrieved nodes
  highlighted (saved to `rag3_simple.png`).

### Confidence-gated RAG with citations (RAG 4.0)
- **[w3_d4_confidence_ex1.py](w3_d4_confidence_ex1.py)** — Smallest possible
  example of confidence gating in isolation: embed a query and a few
  candidate documents, average the top-k cosine similarities into a single
  confidence score, and print either a fallback message or a "proceed"
  message depending on whether it clears a threshold. No LLM call.
- **[w3_d4_demo.py](w3_d4_demo.py)** — Adds a confidence-gating step before
  generation: retrieves the top match from a small knowledge base, computes a
  similarity-based confidence score, and only calls the LLM (via the raw
  `openai` SDK) if confidence clears a threshold — otherwise it returns a
  "not confident enough" response instead of guessing. Answers are generated
  with inline source citations (e.g. `[RefundPolicy.pdf]`). Falls back to
  printing the prompt instead of calling the API if no key is set. Requires
  an OpenAI API key.

## Setup

A virtual environment is already set up in `.venv`. To install/update
dependencies:

```bash
python3 -m venv .venv          # only needed if .venv doesn't exist yet
./.venv/bin/pip install -r requirements.txt
```

Core dependencies used across these scripts:

```
sentence-transformers
torch
numpy
networkx
matplotlib
langchain-core
langchain-text-splitters
langchain-community
langchain-huggingface
faiss-cpu
chromadb        # w2_d4_vector_db_example3.py only
langchain-openai  # w3_d1_rag_demo.py and w3_d2_rag2_demo.py only
openai            # w3_d4_demo.py only (uses the OpenAI SDK directly)
```

### API keys

`w3_d1_rag_demo.py`, `w3_d2_rag2_demo.py`, and `w3_d4_demo.py` call the
OpenAI API and expect a key in the `my_api_key` / `api_key` variable at the
top of the file. **Do not commit real API keys.** Prefer setting
`OPENAI_API_KEY` as an environment variable or loading it from a `.env` file
(untracked) instead of hardcoding it before pushing this repo to GitHub.

## Running a script

```bash
./.venv/bin/python w3_d3_rag3_simple_rerank.py
```

## AI usage declaration

AI assistance (Claude, via Claude Code) was used in preparing this repo, specifically for:

- Writing the per-file summaries in the "Topics by file" section above, based on reading the existing scripts.
- Generating `requirements.txt` from the project's installed dependencies.
- Installing project dependencies (matplotlib, openai) into the local virtual environment.
- Initializing the git repository and creating/pushing this GitHub repo.

The Python scripts themselves are the author's own study work from the PGDip course.
AI was not used to write or modify the code in the `.py` files, and was not used to
generate or handle any real API keys or credentials — the `my_api_key` placeholders
are intentionally left blank (see the API keys note above).
