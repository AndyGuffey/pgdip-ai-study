# PGDip Study Code — RAG & LLM Security

Running collection of study scripts exploring vector search, embeddings,
Retrieval-Augmented Generation (RAG), and LLM security, organized by course
week (`week2_embeddings_and_generation/`, `week3_rag/`,
`week4_agents_and_safety/`, `week5_strategy_risk_governance/`,
`week6_discovery_design_build/`), with each file prefixed by the day it
covers within that week (`d1_`, `d2_`, ...).

## Topics by file

Click a topic to expand it and see the file-by-file details.

<details>
<summary><strong>Model evaluation & benchmarking</strong></summary>

- **[week2_embeddings_and_generation/d1_sentiment_model_comparison.py](week2_embeddings_and_generation/d1_sentiment_model_comparison.py)**
  — Compares two pretrained sentiment-analysis models — a general SST-2
  model and one fine-tuned specifically on IMDB — against the same 60 IMDB
  test reviews, scores each against the dataset's gold labels, and prints a
  mini leaderboard ranking the models by accuracy.

</details>

<details>
<summary><strong>Constrained generation / decoding controls</strong></summary>

- **[week2_embeddings_and_generation/d2_constrained_generation_demo.py](week2_embeddings_and_generation/d2_constrained_generation_demo.py)**
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

- **[week2_embeddings_and_generation/d2_json_schema_validation.py](week2_embeddings_and_generation/d2_json_schema_validation.py)** —
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

- **[week2_embeddings_and_generation/d3_embedding_similarity.py](week2_embeddings_and_generation/d3_embedding_similarity.py)** —
  Smallest possible illustration of embeddings: encode three sentences with
  `sentence-transformers` and print the full pairwise cosine-similarity
  matrix, showing that two semantically similar sentences score much
  higher against each other than either does against an unrelated one.
- **[week2_embeddings_and_generation/d3_chunk_demo.py](week2_embeddings_and_generation/d3_chunk_demo.py)** — Standalone demo of the first half
  of a RAG pipeline: word-based chunking with overlap, embedding chunks with
  `sentence-transformers`, and cosine-similarity search over the resulting
  vectors. No vector database or LLM involved — good for seeing chunking and
  semantic search in isolation.

</details>

<details>
<summary><strong>Vector databases</strong></summary>

- **[week2_embeddings_and_generation/d4_vector_db_example3.py](week2_embeddings_and_generation/d4_vector_db_example3.py)** — Using
  ChromaDB as a vector store: embedding + storing documents with rich
  metadata, querying with relevance scoring, filtering results by an
  access-control field (`sensitivity`), and sharding a collection across
  multiple ChromaDB collections for scale.

</details>

<details>
<summary><strong>RAG basics (RAG 1.0)</strong></summary>

- **[week3_rag/d1_rag_example_1.py](week3_rag/d1_rag_example_1.py)** — Minimal RAG example:
  embed a few sentences with `HuggingFaceEmbeddings`, store them in FAISS,
  and retrieve the top matches for a query. Retrieval only, no generation.
- **[week3_rag/d1_rag_demo.py](week3_rag/d1_rag_demo.py)** — Full end-to-end RAG pipeline:
  document chunking (`RecursiveCharacterTextSplitter`) → embeddings → FAISS
  vector store → retriever → OpenAI LLM (`gpt-4o-mini`) → generated,
  source-traceable answer. Requires an OpenAI API key.

</details>

<details>
<summary><strong>Hybrid retrieval (RAG 2.0)</strong></summary>

- **[week3_rag/d2_rag2_demo.py](week3_rag/d2_rag2_demo.py)** — Combines sparse keyword
  search (BM25) with dense vector search (FAISS) into a simple hybrid
  retriever, compares results from each method side by side, then feeds the
  merged context to an OpenAI LLM for answer generation. Requires an OpenAI
  API key.

</details>

<details>
<summary><strong>Reranking & graph retrieval (RAG 3.0)</strong></summary>

- **[week3_rag/d3_rag3_reranking_ex.py](week3_rag/d3_rag3_reranking_ex.py)** — Smallest
  possible reranking example: score a fixed list of retrieved documents
  against a query using a `CrossEncoder` and print them in relevance order.
- **[week3_rag/d3_rag3_example.py](week3_rag/d3_rag3_example.py)** — Builds a document
  similarity graph with `networkx` (edges added when cosine similarity
  exceeds a threshold) and visualizes it with `matplotlib`.
- **[week3_rag/d3_rag3_simple_rerank.py](week3_rag/d3_rag3_simple_rerank.py)** — Puts it
  all together: a `SimpleRAG3` class that retrieves candidates via
  knowledge-graph traversal (embeddings + manually defined document
  connections), reranks them with a `CrossEncoder`, assembles a context
  string, and renders the knowledge graph with the retrieved nodes
  highlighted (saved to `rag3_simple.png`).

</details>

<details>
<summary><strong>Confidence-gated RAG with citations (RAG 4.0)</strong></summary>

- **[week3_rag/d4_confidence_ex1.py](week3_rag/d4_confidence_ex1.py)** — Smallest possible
  example of confidence gating in isolation: embed a query and a few
  candidate documents, average the top-k cosine similarities into a single
  confidence score, and print either a fallback message or a "proceed"
  message depending on whether it clears a threshold. No LLM call.
- **[week3_rag/d4_demo.py](week3_rag/d4_demo.py)** — Adds a confidence-gating step before
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

- **[week4_agents_and_safety/d1_local_llm_injection.py](week4_agents_and_safety/d1_local_llm_injection.py)** —
  Demonstrates a **vulnerable** prompt design against a local `gpt2` model
  (loaded via `transformers`): a "secret" is embedded directly in a plain-text
  prompt with no role separation, so it can potentially be leaked through
  prompt injection in the interactive chat loop. Intended as a security
  anti-pattern to study, not a template to copy.
- **[week4_agents_and_safety/d1_openai_safe.py](week4_agents_and_safety/d1_openai_safe.py)** — The same "don't reveal
  the secret code" scenario, but built on OpenAI's chat completions API using
  a proper `system` role instead of concatenating everything into one prompt
  string. Useful for comparing role-separated prompting against the naive
  approach in `week4_agents_and_safety/d1_local_llm_injection.py` — note that a system prompt
  alone is still not a complete defense against injection. Requires an
  OpenAI API key.
- **[week4_agents_and_safety/d1_prompt_fuzzing_script.py](week4_agents_and_safety/d1_prompt_fuzzing_script.py)** —
  Prompt fuzzing: a batch of known injection/jailbreak strings (system
  prompt extraction, instruction override, "ignore restrictions", etc.) run
  through an LLM in a loop so responses can be reviewed for guardrail
  failures, rather than testing one attack prompt at a time. **Note:** this
  is a snippet that calls a `run_llm(...)` function which isn't defined in
  the file — wire it up to one of the `ask_llm` / `ask_local_llm` functions
  from the other `week4_agents_and_safety/d1_*` scripts (or your own) before
  running it.

</details>

<details>
<summary><strong>Agents: plan → act → check</strong></summary>

- **[week4_agents_and_safety/d2_example1.py](week4_agents_and_safety/d2_example1.py)** — Smallest possible example of
  agent state/memory: a key-value store an agent can write to (`remember`)
  and read from (`recall`) across a session, instead of relying only on
  what's in the current prompt/context.
- **[week4_agents_and_safety/d2_retry_backoff.py](week4_agents_and_safety/d2_retry_backoff.py)** — Standalone example
  of the retry-with-exponential-backoff reliability pattern used by
  `week4_agents_and_safety/d2_full_demo.py`: retries a flaky mock API call up to 3 times,
  waiting progressively longer (`2 ** attempt` seconds) between attempts
  instead of retrying instantly or failing immediately.
- **[week4_agents_and_safety/d2_small_agent.py](week4_agents_and_safety/d2_small_agent.py)** — Minimal single-tool
  agent demonstrating the basic **plan → act → check** loop: an LLM plans
  which tool to use for a query, the code calls a mocked `get_weather` tool
  based on that plan, then checks the result before returning a final
  answer. Requires an OpenAI API key.
- **[week4_agents_and_safety/d2_full_demo.py](week4_agents_and_safety/d2_full_demo.py)** — Fuller single-agent demo
  building on the same plan → act → check loop, adding: two mock tools
  (`get_weather`, `check_calendar`), reliability via `retry_with_backoff`
  (retries with exponential backoff for flaky tool calls), the
  `AgentState` memory pattern from `week4_agents_and_safety/d2_example1.py` (remembers
  `preferred_city` between turns), and a graceful fallback response when a
  tool fails or no tool matches. Runs as an interactive loop. Requires an
  OpenAI API key.

</details>

<details>
<summary><strong>Multi-agent orchestration</strong></summary>

- **[week4_agents_and_safety/d3_message_passing.py](week4_agents_and_safety/d3_message_passing.py)** — Smallest
  possible sketch of the Planner → Executor → Verifier shape: each stage is
  a plain function that takes the previous stage's string output and
  returns a new string, with no LLM calls. Good for seeing the message-
  passing shape of the pipeline before adding real agents.
- **[week4_agents_and_safety/d3_agent_disagree.py](week4_agents_and_safety/d3_agent_disagree.py)** — Smallest
  possible illustration of agent disagreement: two "agents" compute the
  same thing slightly differently (`x * 2` vs `x * 2.0001`), producing
  different answers for the same input. No LLM involved — a starting point
  for thinking about how an orchestrator should detect and resolve
  disagreement between agents.
- **[week4_agents_and_safety/d3_deadlock_example.py](week4_agents_and_safety/d3_deadlock_example.py)** — Simplified
  illustration of a deadlock between agents: Planner, Executor, and
  Verifier are each waiting on one another to proceed, and a repeated-
  message count is used as a simple signal to detect the deadlock and
  break out of the loop. No LLM involved.
- **[week4_agents_and_safety/d3_multi_agent_demo.py](week4_agents_and_safety/d3_multi_agent_demo.py)** — Three
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

- **[week4_agents_and_safety/d4_open_ai_fun_call.py](week4_agents_and_safety/d4_open_ai_fun_call.py)** — Just the
  tool schema half of function calling: defines an `add_numbers(a, b)`
  tool spec (JSON-schema-style `parameters`) in the shape the OpenAI API
  expects, with no client call or execution logic. Useful as a minimal
  reference for the schema shape before wiring it into a real request.
- **[week4_agents_and_safety/d4_toy_calc_tool.py](week4_agents_and_safety/d4_toy_calc_tool.py)** — Full round trip of
  OpenAI function/tool calling: defines an `add` tool, sends a user message
  to `gpt-4o-mini` with that tool available, executes the tool locally when
  the model requests a call, feeds the result back into the conversation as
  a `tool` message, and asks the model for a final answer informed by the
  result. Loads `OPENAI_API_KEY` from a `.env` file via `python-dotenv`.
  Requires an OpenAI API key.
- **[week4_agents_and_safety/d4_2_tools.py](week4_agents_and_safety/d4_2_tools.py)** — Offering the model a _choice_
  of tools: `get_weather` and `get_client_details` are both provided in the
  same request, and the model picks which one (if any) fits a free-typed
  user question; the chosen tool is then executed via an `if`/`elif` on the
  returned function name. Loads `OPENAI_API_KEY` from a `.env` file via
  `python-dotenv`. Requires an OpenAI API key.
- **[week4_agents_and_safety/d4_dynamic_tools.py](week4_agents_and_safety/d4_dynamic_tools.py)** — Same idea as
  `week4_agents_and_safety/d4_2_tools.py`, but tools are registered at runtime via a
  `register_tool()` helper into a name → function `TOOL_REGISTRY` and a
  matching list of schemas, so the model's chosen tool can be looked up and
  called generically (`TOOL_REGISTRY[func_name](**args)`) instead of an
  `if`/`elif` chain per tool. Loads `OPENAI_API_KEY` from a `.env` file via
  `python-dotenv`. Requires an OpenAI API key.

</details>

<details>
<summary><strong>Agent observability & tracing</strong></summary>

- **[week4_agents_and_safety/d4_real_trace_example.py](week4_agents_and_safety/d4_real_trace_example.py)** — Not a
  runnable script: a sample trace record showing what an agent
  observability/tracing log entry should capture when an agent decides to
  call a tool — timestamp, role, decision type, the chosen tool and its
  arguments, and a `run_id` to correlate it with the rest of that session's
  trace.
- **[week4_agents_and_safety/d4_simple_trace_logger.py](week4_agents_and_safety/d4_simple_trace_logger.py)** — A
  minimal, reusable trace logger: `log_event()` stamps an event dict with
  the current time and appends it as a JSON line to `trace.log`, building
  an on-disk, replayable record of an agent's decisions/actions.
- **[week4_agents_and_safety/d4_tool_call_trace_logging.py](week4_agents_and_safety/d4_tool_call_trace_logging.py)**
  — Wraps a real tool (`get_weather`) so every call and its result are
  logged via `log_event` (imported from `week4_agents_and_safety/d4_simple_trace_logger.py`),
  showing where trace logging hooks into an actual tool rather than just
  the log entry shape.
- **[week4_agents_and_safety/d4_logging_llm_decisions.py](week4_agents_and_safety/d4_logging_llm_decisions.py)** —
  Wraps an OpenAI chat completion call so the model's decision (which tool
  it chose, or that it responded directly) is logged as a trace event
  alongside the response, again via `log_event`. Requires an OpenAI API
  key.
- **[week4_agents_and_safety/d4_full_demo.py](week4_agents_and_safety/d4_full_demo.py)** — Combines OpenAI
  function/tool calling with tracing in one script: an `add` tool is
  offered to `gpt-4o-mini`, the model decides whether to call it, the tool
  executes locally, and every step (the user message, the model's
  decision, and each tool call/result) is logged as a JSON-line trace
  event. Loads `OPENAI_API_KEY` from a `.env` file via `python-dotenv`.
  Requires an OpenAI API key.

</details>

<details>
<summary><strong>Local LLM inference</strong></summary>

- **[week5_strategy_risk_governance/d1_example1.py](week5_strategy_risk_governance/d1_example1.py)** —
  Runs a quantized, fully offline model (Phi-2, `.gguf` format) via
  `llama-cpp-python`, prompting it for code explanation, a technical Q&A
  answer, a short creative-writing piece, and a problem-solving list — no
  API key or network call involved. Requires a local
  `phi-2.Q4_K_M.gguf` model file in the same directory.
- **[week5_strategy_risk_governance/d1_example2.py](week5_strategy_risk_governance/d1_example2.py)** —
  Same idea, different approach: calls a local Phi model through
  [Ollama](https://ollama.com)'s HTTP API (`http://localhost:11434/api/generate`)
  via `requests` instead of loading the model in-process, with error
  handling for the Ollama server not running, the request timing out, or
  the call being interrupted. Requires Ollama running locally
  (`ollama serve`) with the `phi` model pulled.

</details>

<details>
<summary><strong>Inference performance measurement</strong></summary>

- **[week5_strategy_risk_governance/d2_inference_performance_ex1.py](week5_strategy_risk_governance/d2_inference_performance_ex1.py)**
  — Smallest possible latency measurement: sends one prompt to OpenAI's
  `gpt-4o-mini` and times the full request-to-response call with
  `time.time()`. Requires an OpenAI API key.
- **[week5_strategy_risk_governance/d2_inference_performance_ex2.py](week5_strategy_risk_governance/d2_inference_performance_ex2.py)**
  — No LLM involved: simulates a small neural network's forward pass
  (linear layer → ReLU → linear layer) over increasing batch sizes using
  vectorized NumPy operations, timing each batch to show how real batched
  inference scales with batch size.
- **[week5_strategy_risk_governance/d2_inference_performance_ex3.py](week5_strategy_risk_governance/d2_inference_performance_ex3.py)**
  — Streams the same prompt to `gpt-4o-mini` three times, measuring
  time-to-first-token (TTFT), total time, and tokens/sec per run, then
  compares Run 2 against Run 1 to check for (and explain the absence of)
  response caching between independent OpenAI API calls. Requires an
  OpenAI API key.

</details>

<details>
<summary><strong>KV cache, paged attention & speculative decoding</strong></summary>

- **[week5_strategy_risk_governance/d3_kv_cache_memory_calc.py](week5_strategy_risk_governance/d3_kv_cache_memory_calc.py)** —
  Calculates KV cache memory footprint (in MB) for a given transformer
  shape (layers, heads, head dimension) across a few sequence lengths, with
  no actual inference — just the arithmetic behind why long-context serving
  is memory-bound.
- **[week5_strategy_risk_governance/d3_paged_attention_sim.py](week5_strategy_risk_governance/d3_paged_attention_sim.py)** —
  Toy simulation of paged KV cache allocation: tokens are packed into
  fixed-size blocks ("pages") instead of one contiguous buffer, starting a
  new page once the current one fills up — the core idea behind vLLM-style
  paged attention.
- **[week5_strategy_risk_governance/d3_speculative_decoding_openai.py](week5_strategy_risk_governance/d3_speculative_decoding_openai.py)** —
  Real speculative decoding against the OpenAI API: a fast draft model
  (`gpt-3.5-turbo`) proposes several one-word continuations, and a slower,
  more accurate main model (`gpt-4o-mini`) scores each and either accepts a
  good one or generates its own replacement. Requires an OpenAI API key.
- **[week5_strategy_risk_governance/d3_inference_optimizations_demo.py](week5_strategy_risk_governance/d3_inference_optimizations_demo.py)** —
  Combined, self-contained demo of all three techniques with timed
  before/after comparisons: naive vs. KV-cached attention, a
  `PagedAttentionManager` allocating/evicting fixed-size memory pages
  across simulated chat sessions, and mocked draft/target models comparing
  sequential vs. speculative-decoding generation speed. No API key needed
  — everything is simulated locally.

</details>

<details>
<summary><strong>Cost-aware & resilient model serving</strong></summary>

- **[week5_strategy_risk_governance/d4_model_serve_ex1.py](week5_strategy_risk_governance/d4_model_serve_ex1.py)** —
  Confidence-gated SLM→LLM fallback: a cheap small language model answers
  every prompt with a (faked, for demo purposes) confidence score, and only
  escalates to a more expensive LLM when confidence falls below a
  threshold. Prints a per-query trace plus a cost comparison against
  always using the LLM.
- **[week5_strategy_risk_governance/d4_model_serve_ex2.py](week5_strategy_risk_governance/d4_model_serve_ex2.py)** —
  Retry-then-fallback resilience: an unreliable SLM that randomly times
  out is retried a couple of times before falling back to a slower but
  dependable LLM, run across multiple trials to show the SLM succeeding
  sometimes and falling back on others.

</details>

<details>
<summary><strong>Agent memory patterns</strong></summary>

- **[week6_discovery_design_build/d1_memory_types_ex1.py](week6_discovery_design_build/d1_memory_types_ex1.py)** —
  Contrasts short-term memory (an in-process dict holding just the last
  message, cleared between sessions) with long-term memory (a user
  preference persisted to `memory.json` across sessions), combining both
  in a single chat response.
- **[week6_discovery_design_build/d1_memory_type_ex2.py](week6_discovery_design_build/d1_memory_type_ex2.py)** —
  Memory with a Time-To-Live (TTL): each stored value carries an expiry
  timestamp, and reading it lazily deletes and returns `None` once that
  timestamp has passed, instead of relying on manual cleanup.
- **[week6_discovery_design_build/d1_memory_types_ex3.py](week6_discovery_design_build/d1_memory_types_ex3.py)** —
  Consent-aware memory: every write is gated behind an explicit
  yes/no prompt asking the user's permission before the value is stored,
  demonstrated with a mix of consented and declined test data.

</details>

<details>
<summary><strong>ML ops: reproducibility, versioning & regression testing</strong></summary>

- **[week6_discovery_design_build/d2_reproducibility_ex1.py](week6_discovery_design_build/d2_reproducibility_ex1.py)** —
  Trains a trivial "model" (the average of 5 random numbers) with and
  without a fixed random seed, showing unseeded runs produce different
  scores each time while seeded runs reproduce the exact same score —
  a minimal illustration of why reproducibility matters in ML ops.
- **[week6_discovery_design_build/d2_data_versioning_ex2.py](week6_discovery_design_build/d2_data_versioning_ex2.py)** —
  Dataset versioning via content hashing: MD5-hashes two near-identical
  dataset versions to show a single changed value produces a completely
  different hash, then splits a dataset into train/eval slices.
- **[week6_discovery_design_build/d2_experiment_versioning_ex3.py](week6_discovery_design_build/d2_experiment_versioning_ex3.py)** —
  Builds on `week6_discovery_design_build/d2_data_versioning_ex2.py`'s dataset
  hashing: combines a dataset hash with model hyperparameters and a code
  version into a single short experiment version ID, showing different
  data/hyperparameters produce different IDs while identical inputs
  reproduce the same one.
- **[week6_discovery_design_build/d2_ml_ops_ex4.py](week6_discovery_design_build/d2_ml_ops_ex4.py)** —
  ML regression testing: asserts a model's evaluation metrics (accuracy,
  latency, bias gap) against fixed quality thresholds, run against a
  passing model, an accuracy regression, and a latency regression to show
  how each failure is caught before deployment.
- **[week6_discovery_design_build/d2_ml_ops_ex5.py](week6_discovery_design_build/d2_ml_ops_ex5.py)** —
  A fuller regression testing example than `d2_ml_ops_ex4.py`: a mocked
  sentiment classifier with three versions (baseline, improved,
  deliberately regressed) is each run over a fixed test set and scored on
  average confidence/latency against pass/fail thresholds, blocking
  deployment of the regressed version.

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
chromadb        # week2_embeddings_and_generation/d4_vector_db_example3.py only
langchain-openai  # week3_rag/d1_rag_demo.py and week3_rag/d2_rag2_demo.py only
openai            # week3_rag/d4_demo.py, week4_agents_and_safety/d1_openai_safe.py, week4_agents_and_safety/d2_small_agent.py, week4_agents_and_safety/d2_full_demo.py, week4_agents_and_safety/d3_multi_agent_demo.py, week4_agents_and_safety/d4_toy_calc_tool.py, week4_agents_and_safety/d4_2_tools.py, week4_agents_and_safety/d4_dynamic_tools.py, week4_agents_and_safety/d4_logging_llm_decisions.py, week4_agents_and_safety/d4_full_demo.py, week5_strategy_risk_governance/d2_inference_performance_ex1.py, week5_strategy_risk_governance/d2_inference_performance_ex3.py, week5_strategy_risk_governance/d3_speculative_decoding_openai.py (uses the OpenAI SDK directly)
transformers      # week4_agents_and_safety/d1_local_llm_injection.py only (local gpt2 model)
python-dotenv     # week4_agents_and_safety/d3_multi_agent_demo.py, week4_agents_and_safety/d4_toy_calc_tool.py, week4_agents_and_safety/d4_2_tools.py, week4_agents_and_safety/d4_dynamic_tools.py, week4_agents_and_safety/d4_full_demo.py, week5_strategy_risk_governance/d2_inference_performance_ex1.py, week5_strategy_risk_governance/d2_inference_performance_ex3.py, week5_strategy_risk_governance/d3_speculative_decoding_openai.py only (loads OPENAI_API_KEY from a .env file)
llama-cpp-python  # week5_strategy_risk_governance/d1_example1.py only (runs a local GGUF model via llama.cpp bindings)
requests          # week5_strategy_risk_governance/d1_example2.py only (calls a local Ollama server's HTTP API)
```

### API keys

`week3_rag/d1_rag_demo.py`, `week3_rag/d2_rag2_demo.py`, `week3_rag/d4_demo.py`,
`week4_agents_and_safety/d1_openai_safe.py`, `week4_agents_and_safety/d2_small_agent.py`, and `week4_agents_and_safety/d2_full_demo.py`
call the OpenAI API and expect a key in the `my_api_key` / `api_key`
variable at the top of the file. **Do not commit real API keys.** Prefer
setting `OPENAI_API_KEY` as an environment variable or loading it from a
`.env` file (untracked) instead of hardcoding it before pushing this repo
to GitHub.

`week4_agents_and_safety/d3_multi_agent_demo.py`, `week4_agents_and_safety/d4_toy_calc_tool.py`, `week4_agents_and_safety/d4_2_tools.py`,
`week4_agents_and_safety/d4_dynamic_tools.py`, and `week4_agents_and_safety/d4_full_demo.py` already follow that
recommendation: they load `OPENAI_API_KEY` from a `.env` file (untracked,
via `python-dotenv`) instead of a hardcoded variable — create a `.env` file
with `OPENAI_API_KEY=your-api-key-here` before running them.

`week4_agents_and_safety/d4_logging_llm_decisions.py` calls `OpenAI()` with no explicit key
argument, so it relies on `OPENAI_API_KEY` already being set as an
environment variable (it doesn't call `load_dotenv()` itself) — export it
in your shell, or `source` a `.env` file, before running it.

`week4_agents_and_safety/d1_local_llm_injection.py` runs entirely locally (downloads `gpt2` via
`transformers` on first run) and needs no API key.

`week5_strategy_risk_governance/d1_example1.py` also runs entirely locally
(a quantized Phi-2 model loaded via `llama-cpp-python`) and needs no API
key — but it does need the `phi-2.Q4_K_M.gguf` model file present in that
directory.

`week5_strategy_risk_governance/d1_example2.py` also needs no API key — it
calls a local Ollama server instead of a hosted API. It does need Ollama
installed and running (`ollama serve`) with the `phi` model pulled first.

`week5_strategy_risk_governance/d2_inference_performance_ex1.py` and
`week5_strategy_risk_governance/d2_inference_performance_ex3.py` also load
`OPENAI_API_KEY` from a `.env` file (untracked, via `python-dotenv`) —
create a `.env` file with `OPENAI_API_KEY=your-api-key-here` before running
them.

`week5_strategy_risk_governance/d2_inference_performance_ex2.py` runs
entirely locally (a NumPy-simulated forward pass, no LLM call) and needs no
API key.

`week5_strategy_risk_governance/d3_speculative_decoding_openai.py` also loads `OPENAI_API_KEY`
from a `.env` file (untracked, via `python-dotenv`) — create a `.env` file
with `OPENAI_API_KEY=your-api-key-here` before running it.

`week5_strategy_risk_governance/d3_kv_cache_memory_calc.py`, `d3_paged_attention_sim.py`, and `d3_inference_optimizations_demo.py`
run entirely locally (arithmetic, a toy paging simulation, and mocked
draft/target models respectively — no real LLM calls) and need no API
key.

`week4_agents_and_safety/d4_open_ai_fun_call.py`, `week4_agents_and_safety/d4_real_trace_example.py`,
`week4_agents_and_safety/d4_simple_trace_logger.py`, and `week4_agents_and_safety/d4_tool_call_trace_logging.py` don't
call the OpenAI API at all, so none of them need a key.

`week4_agents_and_safety/d4_open_ai_fun_call.py` only defines a tool schema — it doesn't call the
OpenAI API and needs no key.

## Running a script

```bash
./.venv/bin/python week3_rag/d3_rag3_simple_rerank.py
```

## AI usage declaration

AI assistance (Claude, via Claude Code) was used in preparing this repo, specifically for:

- Writing the per-file summaries in the "Topics by file" section above, based on reading the existing scripts.
- Generating `requirements.txt` from the project's installed dependencies.
- Installing project dependencies (matplotlib, openai) into the local virtual environment.
- Initializing the git repository and creating/pushing this GitHub repo.
