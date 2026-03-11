# RAG Pipeline

!!! info "Planned Architecture (Future Phases)"
    The RAG pipeline is implemented in **Phase 3** (Weeks 8–11).

---

## Overview

<!-- Describe what the RAG pipeline does: index financial documents, retrieve relevant context, inject into LLM prompts -->

---

## Indexing

### Document Chunking

<!-- Describe chunking strategy: chunk size (512 tokens), overlap (64 tokens), metadata attachment -->

```python
# Chunking configuration
CHUNK_SIZE = 512
CHUNK_OVERLAP = 64
METADATA_FIELDS = ["company_id", "filing_id", "period", "section"]
```

### Embedding Model

<!-- Describe embedding model choice: OpenAI text-embedding-3-small / sentence-transformers -->

### Indexing Pipeline

<!-- Describe how chunks are embedded and inserted into pgvector, batch processing, re-index trigger -->

---

## Retrieval

### Dense Retrieval (pgvector)

<!-- Describe cosine similarity query, top-k selection, minimum score threshold -->

```sql
SELECT content, 1 - (embedding <=> $1::vector) AS score
FROM document_chunks
ORDER BY embedding <=> $1::vector
LIMIT 10;
```

### Sparse Retrieval (Elasticsearch)

!!! info "Planned Architecture (Future Phases)"
    Elasticsearch hybrid retrieval is implemented in Phase 3.

<!-- Describe BM25 query on `content` field, field boosting for financial term keywords -->

### Hybrid Fusion

<!-- Describe Reciprocal Rank Fusion (RRF): score = 1/(k + rank), final top-k selection -->

---

## Generation

### Context Injection

<!-- Describe prompt template: system instructions, retrieved chunks formatted with citations, user query -->

### LLM Configuration

<!-- Describe model selection (GPT-4o / Claude), temperature settings, max_tokens, structured output -->

---

## Evaluation

<!-- Describe RAG evaluation metrics: faithfulness, context relevance, answer completeness -->
