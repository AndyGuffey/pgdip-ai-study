# PGDip Study Code — RAG & LLM Security

Running collection of study scripts exploring vector search, embeddings,
Retrieval-Augmented Generation (RAG), and LLM security, roughly ordered by
week/day as covered in the course (`w2_d1`, `w2_d2`, `w2_d4`, `w3_d1`,
`w3_d2`, `w3_d3`, `w3_d4`, `w4_d1`, `w4_d2`, ...).

## Topics by file

Click a topic to expand it and see the file-by-file details.

<details>
<summary><strong>Model evaluation & benchmarking</strong></summary>

- **[w2_d1_sentiment_model_comparison.py](w2_d1_sentiment_model_comparison.py)**
  — Compares two pretrained sentiment-analysis models — a general SST-2
  model and one fine-tuned specifically on IMDB — against the same 60 IMDB
  test reviews, scores each against the dataset's gold labels, and prints a
  mini leaderboard ranking the models by accuracy.

</details>

<details>
<summary><strong>Constrained generation / decoding controls</strong></summary>

- **[w2_d2_constrained_generation_demo.py](w2_d2_constrained_generation_demo.py)**
  — Runs the same prompt through a local `gpt2` model twice: once with
  sampling and a higher token budget (unconstrained, more varied/rambling
  output) and once with greedy decoding and a tight token cap (constrained,
  short and deterministic), showing how generation parameters
  (`max_new_tokens`, `do_sample`, `temperature`) shape output. Includes
  commented-out sketches of further temperature-control and hard
  length-constraint experiments.

</details>

<details>
<summary><strong>Structured output validation & repair</strong></summary>

- **[w2_d2_json_schema_validation.py](w2_d2_json_schema_validation.py)** —
  Validates a flawed, LLM-style JSON product record against a strict JSON
  Schema (`jsonschema`, `Draft202012Validator`) that catches type
  mismatches, disallowed enum values, and extra fields, then attempts to
  auto-correct common mistakes (a string price with a currency symbol, a
  non-standard currency code, inconsistent casing, non-string tags) and
  re-validates — printing before/after diagnostics either way. Also
  includes a small helper to strip JavaScript-style `//` comments that
  LLMs sometimes add to otherwise-valid JSON.

</details>

<details>
<summary><strong>Chunking & embeddings</strong></summary>

- **[d3_chunk_demo.py](d3_chunk_demo.py)** — Standalone demo of the first half
  of a RAG pipeline: word-based chunking with overlap, embedding chunks with
  `sentence-transformers`, and cosine-similarity search over the resulting
  vectors. No vector database or LLM involved — good for seeing chunking and
  semantic search in isolation.

</details>

<details>
<summary><strong>Vector databases</strong></summary>

- **[w2_d4_vector_db_example3.py](w2_d4_vector_db_example3.py)** — Using
  ChromaDB as a vector store: embedding + storing documents with rich
  metadata, querying with relevance scoring, filtering results by an
  access-control field (`sensitivity`), and sharding a collection across
  multiple ChromaDB collections for scale.

</details>

<details>
<summary><strong>RAG basics (RAG 1.0)</strong></summary>

- **[w3_d1_rag_example_1.py](w3_d1_rag_example_1.py)** — Minimal RAG example:
  embed a few sentences with `HuggingFaceEmbeddings`, store them in FAISS,
  and retrieve the top matches for a query. Retrieval only, no generation.
- **[w3_d1_rag_demo.py](w3_d1_rag_demo.py)** — Full end-to-end RAG pipeline:
  document chunking (`RecursiveCharacterTextSplitter`) → embeddings → FAISS
  vector store → retriever → OpenAI LLM (`gpt-4o-mini`) → generated,
  source-traceable answer. Requires an OpenAI API key.

</details>

<details>
<summary><strong>Hybrid retrieval (RAG 2.0)</strong></summary>

- **[w3_d2_rag2_demo.py](w3_d2_rag2_demo.py)** — Combines sparse keyword
  search (BM25) with dense vector search (FAISS) into a simple hybrid
  retriever, compares results from each method side by side, then feeds the
  merged context to an OpenAI LLM for answer generation. Requires an OpenAI
  API key.

</details>

<details>
<summary><strong>Reranking & graph retrieval (RAG 3.0)</strong></summary>

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

</details>

<details>
<summary><strong>Confidence-gated RAG with citations (RAG 4.0)</strong></summary>

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

</details>

<details>
<summary><strong>LLM security: prompt injection & fuzzing</strong></summary>

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

</details>

<details>
<summary><strong>Agents: plan → act → check</strong></summary>

- **[w4_d2_example1.py](w4_d2_example1.py)** — Smallest possible example of
  agent state/memory: a key-value store an agent can write to (`remember`)
  and read from (`recall`) across a session, instead of relying only on
  what's in the current prompt/context.
- **[w4_d2_retry_backoff.py](w4_d2_retry_backoff.py)** — Standalone example
  of the retry-with-exponential-backoff reliability pattern used by
  `w4_d2_full_demo.py`: retries a flaky mock API call up to 3 times,
  waiting progressively longer (`2 ** attempt` seconds) between attempts
  instead of retrying instantly or failing immediately.
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

</details>

<details>
<summary><strong>Multi-agent orchestration</strong></summary>

- **[w4_d3_message_passing.py](w4_d3_message_passing.py)** — Smallest
  possible sketch of the Planner → Executor → Verifier shape: each stage is
  a plain function that takes the previous stage's string output and
  returns a new string, with no LLM calls. Good for seeing the message-
  passing shape of the pipeline before adding real agents.
- **[w4_d3_agent_disagree.py](w4_d3_agent_disagree.py)** — Smallest
  possible illustration of agent disagreement: two "agents" compute the
  same thing slightly differently (`x * 2` vs `x * 2.0001`), producing
  different answers for the same input. No LLM involved — a starting point
  for thinking about how an orchestrator should detect and resolve
  disagreement between agents.
- **[w4_d3_deadlock_example.py](w4_d3_deadlock_example.py)** — Simplified
  illustration of a deadlock between agents: Planner, Executor, and
  Verifier are each waiting on one another to proceed, and a repeated-
  message count is used as a simple signal to detect the deadlock and
  break out of the loop. No LLM involved.
- **[w4_d3_multi_agent_demo.py](w4_d3_multi_agent_demo.py)** — Three
  cooperating agents with distinct roles: a **Planner** breaks a task into
  2–4 steps, an **Executor** performs one step at a time against the source
  text, and a **Verifier** checks each result and returns `APPROVE`/`REVISE`,
  triggering one re-attempt from the Executor on a `REVISE` verdict. An
  orchestration loop drives the steps and concatenates the approved results
  into a final answer. Demo task: summarise a paragraph and extract 3 key
  points. Loads `OPENAI_API_KEY` from a `.env` file via `python-dotenv`.
  Requires an OpenAI API key.

</details>

<details>
<summary><strong>OpenAI function/tool calling</strong></summary>

- **[w4_d4_open_ai_fun_call.py](w4_d4_open_ai_fun_call.py)** — Just the
  tool schema half of function calling: defines an `add_numbers(a, b)`
  tool spec (JSON-schema-style `parameters`) in the shape the OpenAI API
  expects, with no client call or execution logic. Useful as a minimal
  reference for the schema shape before wiring it into a real request.
- **[w4_d4_toy_calc_tool.py](w4_d4_toy_calc_tool.py)** — Full round trip of
  OpenAI function/tool calling: defines an `add` tool, sends a user message
  to `gpt-4o-mini` with that tool available, executes the tool locally when
  the model requests a call, feeds the result back into the conversation as
  a `tool` message, and asks the model for a final answer informed by the
  result. Loads `OPENAI_API_KEY` from a `.env` file via `python-dotenv`.
  Requires an OpenAI API key.
- **[w4_d4_2_tools.py](w4_d4_2_tools.py)** — Offering the model a *choice*
  of tools: `get_weather` and `get_client_details` are both provided in the
  same request, and the model picks which one (if any) fits a free-typed
  user question; the chosen tool is then executed via an `if`/`elif` on the
  returned function name. Loads `OPENAI_API_KEY` from a `.env` file via
  `python-dotenv`. Requires an OpenAI API key.
- **[w4_d4_dynamic_tools.py](w4_d4_dynamic_tools.py)** — Same idea as
  `w4_d4_2_tools.py`, but tools are registered at runtime via a
  `register_tool()` helper into a name → function `TOOL_REGISTRY` and a
  matching list of schemas, so the model's chosen tool can be looked up and
  called generically (`TOOL_REGISTRY[func_name](**args)`) instead of an
  `if`/`elif` chain per tool. Loads `OPENAI_API_KEY` from a `.env` file via
  `python-dotenv`. Requires an OpenAI API key.

</details>

<details>
<summary><strong>Agent observability & tracing</strong></summary>

- **[w4_d4_real_trace_example.py](w4_d4_real_trace_example.py)** — Not a
  runnable script: a sample trace record showing what an agent
  observability/tracing log entry should capture when an agent decides to
  call a tool — timestamp, role, decision type, the chosen tool and its
  arguments, and a `run_id` to correlate it with the rest of that session's
  trace.
- **[w4_d4_simple_trace_logger.py](w4_d4_simple_trace_logger.py)** — A
  minimal, reusable trace logger: `log_event()` stamps an event dict with
  the current time and appends it as a JSON line to `trace.log`, building
  an on-disk, replayable record of an agent's decisions/actions.
- **[w4_d4_tool_call_trace_logging.py](w4_d4_tool_call_trace_logging.py)**
  — Wraps a real tool (`get_weather`) so every call and its result are
  logged via `log_event` (imported from `w4_d4_simple_trace_logger.py`),
  showing where trace logging hooks into an actual tool rather than just
  the log entry shape.
- **[w4_d4_logging_llm_decisions.py](w4_d4_logging_llm_decisions.py)** —
  Wraps an OpenAI chat completion call so the model's decision (which tool
  it chose, or that it responded directly) is logged as a trace event
  alongside the response, again via `log_event`. Requires an OpenAI API
  key.
- **[w4_d4_full_demo.py](w4_d4_full_demo.py)** — Combines OpenAI
  function/tool calling with tracing in one script: an `add` tool is
  offered to `gpt-4o-mini`, the model decides whether to call it, the tool
  executes locally, and every step (the user message, the model's
  decision, and each tool call/result) is logged as a JSON-line trace
  event. Loads `OPENAI_API_KEY` from a `.env` file via `python-dotenv`.
  Requires an OpenAI API key.

</details>

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
openai            # w3_d4_demo.py, w4_d1_openai_safe.py, w4_d2_small_agent.py, w4_d2_full_demo.py, w4_d3_multi_agent_demo.py, w4_d4_toy_calc_tool.py, w4_d4_2_tools.py, w4_d4_dynamic_tools.py, w4_d4_logging_llm_decisions.py, w4_d4_full_demo.py (uses the OpenAI SDK directly)
transformers      # w4_d1_local_llm_injection.py only (local gpt2 model)
python-dotenv     # w4_d3_multi_agent_demo.py, w4_d4_toy_calc_tool.py, w4_d4_2_tools.py, w4_d4_dynamic_tools.py, w4_d4_full_demo.py only (loads OPENAI_API_KEY from a .env file)
```

### API keys

`w3_d1_rag_demo.py`, `w3_d2_rag2_demo.py`, `w3_d4_demo.py`,
`w4_d1_openai_safe.py`, `w4_d2_small_agent.py`, and `w4_d2_full_demo.py`
call the OpenAI API and expect a key in the `my_api_key` / `api_key`
variable at the top of the file. **Do not commit real API keys.** Prefer
setting `OPENAI_API_KEY` as an environment variable or loading it from a
`.env` file (untracked) instead of hardcoding it before pushing this repo
to GitHub.

`w4_d3_multi_agent_demo.py`, `w4_d4_toy_calc_tool.py`, `w4_d4_2_tools.py`,
`w4_d4_dynamic_tools.py`, and `w4_d4_full_demo.py` already follow that
recommendation: they load `OPENAI_API_KEY` from a `.env` file (untracked,
via `python-dotenv`) instead of a hardcoded variable — create a `.env` file
with `OPENAI_API_KEY=your-api-key-here` before running them.

`w4_d4_logging_llm_decisions.py` calls `OpenAI()` with no explicit key
argument, so it relies on `OPENAI_API_KEY` already being set as an
environment variable (it doesn't call `load_dotenv()` itself) — export it
in your shell, or `source` a `.env` file, before running it.

`w4_d1_local_llm_injection.py` runs entirely locally (downloads `gpt2` via
`transformers` on first run) and needs no API key.

`w4_d4_open_ai_fun_call.py`, `w4_d4_real_trace_example.py`,
`w4_d4_simple_trace_logger.py`, and `w4_d4_tool_call_trace_logging.py` don't
call the OpenAI API at all, so none of them need a key.

`w4_d4_open_ai_fun_call.py` only defines a tool schema — it doesn't call the
OpenAI API and needs no key.

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
