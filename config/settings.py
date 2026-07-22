# ══════════════════════════════════════════════════════
# config/settings.py — Central configuration
# ══════════════════════════════════════════════════════

# ── Folders ───────────────────────────────────────────
DATA_FOLDER       = "data"           # Drop your .json files here
PERSIST_DIR       = "./storage"      # All persistent indexes saved here
CHROMA_DIR        = "./storage/chroma"
DUCKDB_PATH       = "./storage/duck.db"
BM25_PATH         = "./storage/bm25.pkl"
HASH_PATH         = "./storage/data_hash.txt"

# ── Chunking ──────────────────────────────────────────
CHUNK_SIZE        = 600              # words per chunk
OVERLAP           = 80               # word overlap between chunks

# ── Retrieval ─────────────────────────────────────────
INITIAL_TOP_K     = 20              # candidates before reranking
FINAL_TOP_K       = 5               # chunks after reranking
MMR_LAMBDA        = 0.6             # 0=diversity, 1=relevance
RERANK_MIN_SCORE  = 0.02            # below this → context too weak, fall back to GPT

# ── Models ────────────────────────────────────────────
# Embeddings via Cohere (Groq does not support embeddings)
EMBED_MODEL       = "embed-english-v3.0"
# LLM via Groq (OpenAI-compatible API)
LLM_MODEL         = "llama-3.3-70b-versatile"
ROUTER_MODEL      = "llama-3.1-8b-instant"   # Cheaper + faster for routing/HyDE
COHERE_RERANK     = "rerank-english-v3.0"
# Groq API base URL (used with the openai SDK)
GROQ_BASE_URL     = "https://api.groq.com/openai/v1"

# ── HyDE ─────────────────────────────────────────────
# Only use HyDE if query is vague (fewer than this many words = likely specific)
HYDE_MIN_WORDS    = 6               # queries with < 6 words skip HyDE

# ── Cache ─────────────────────────────────────────────
CACHE_MAX_SIZE    = 200

# ── Embedding batch size ──────────────────────────────
EMBED_BATCH_SIZE  = 100

# ── Web Search (Tavily) ──────────────────────────────
WEB_TOP_K         = 5               # Number of web results to fetch
WEB_SEARCH_KEYWORDS = [             # If these appear in query, prefer web
    "latest", "news", "2025", "2026", "current", "today",
    "update", "recent", "new", "announce",
]
