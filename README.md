# PGDip Study Code — RAG & LLM Security

Running collection of study scripts exploring vector search, embeddings,
Retrieval-Augmented Generation (RAG), and LLM security, roughly ordered by
week/day as covered in the course (`w2_d4`, `w3_d1`, `w3_d2`, `w3_d3`,
`w3_d4`, `w4_d1`, `w4_d2`, ...).

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

### LLM security: prompt injection & fuzzing
- **[w4_d1_local_llm_injection.py](w4_d1_local_llm_injection.py)** —
  Demonstrates a **vulnerable** prompt design against a local `gpt2` model
  (loaded via `transformers`): a "secret" is embedded directly in a plain-text
  prompt with no role separation, so it can potentially be leaked through
  prompt injection in the interactive chat loop. Intended as a security
  anti-pattern to study, not a template to copy.
- **[w4_d1_openai_safe.py](w4_d1_openai_safe.py)** — The same "don't reveal
  the secret code" scenario, but built on OpenAI's chat completions API using
  a proper `system` role instead of concatenating everything into one prompt
  string. Useful for comparing role-separated prompting against the naive
  approach in `w4_d1_local_llm_injection.py` — note that a system prompt
  alone is still not a complete defense against injection. Requires an
  OpenAI API key.
- **[w4_d1_prompt_fuzzing_script.py](w4_d1_prompt_fuzzing_script.py)** —
  Prompt fuzzing: a batch of known injection/jailbreak strings (system
  prompt extraction, instruction override, "ignore restrictions", etc.) run
  through an LLM in a loop so responses can be reviewed for guardrail
  failures, rather than testing one attack prompt at a time. **Note:** this
  is a snippet that calls a `run_llm(...)` function which isn't defined in
  the file — wire it up to one of the `ask_llm` / `ask_local_llm` functions
  from the other `w4_d1_*` scripts (or your own) before running it.

### Agents: plan → act → check
- **[w4_d2_example1.py](w4_d2_example1.py)** — Smallest possible example of
  agent state/memory: a key-value store an agent can write to (`remember`)
  and read from (`recall`) across a session, instead of relying only on
  what's in the current prompt/context.
- **[w4_d2_small_agent.py](w4_d2_small_agent.py)** — Minimal single-tool
  agent demonstrating the basic **plan → act → check** loop: an LLM plans
  which tool to use for a query, the code calls a mocked `get_weather` tool
  based on that plan, then checks the result before returning a final
  answer. Requires an OpenAI API key.
- **[w4_d2_full_demo.py](w4_d2_full_demo.py)** — Fuller single-agent demo
  building on the same plan → act → check loop, adding: two mock tools
  (`get_weather`, `check_calendar`), reliability via `retry_with_backoff`
  (retries with exponential backoff for flaky tool calls), the
  `AgentState` memory pattern from `w4_d2_example1.py` (remembers
  `preferred_city` between turns), and a graceful fallback response when a
  tool fails or no tool matches. Runs as an interactive loop. Requires an
  OpenAI API key.

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
openai            # w3_d4_demo.py, w4_d1_openai_safe.py, w4_d2_small_agent.py, w4_d2_full_demo.py (uses the OpenAI SDK directly)
transformers      # w4_d1_local_llm_injection.py only (local gpt2 model)
```

### API keys

`w3_d1_rag_demo.py`, `w3_d2_rag2_demo.py`, `w3_d4_demo.py`,
`w4_d1_openai_safe.py`, `w4_d2_small_agent.py`, and `w4_d2_full_demo.py`
call the OpenAI API and expect a key in the `my_api_key` / `api_key`
variable at the top of the file. **Do not commit real API keys.** Prefer
setting `OPENAI_API_KEY` as an environment variable or loading it from a
`.env` file (untracked) instead of hardcoding it before pushing this repo
to GitHub.

`w4_d1_local_llm_injection.py` runs entirely locally (downloads `gpt2` via
`transformers` on first run) and needs no API key.

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
