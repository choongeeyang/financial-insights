# LLM Analysis

!!! info "Planned Architecture (Future Phases)"
    The LLM analysis service is implemented in **Phase 3** (Weeks 8–11).

---

## Overview

<!-- Describe the purpose: convert structured financial data + retrieved context into natural language insights -->

---

## Analysis Types

### Company Summary

<!-- Describe: period-specific summary, key highlights, risk flags, generated from filing content -->

### Financial Ratio Commentary

<!-- Describe: auto-generate narrative around P/E, ROE, debt ratios in context of sector benchmarks -->

### Company Comparison

<!-- Describe: side-by-side analysis of two or more companies over the same period -->

### Trend Analysis

<!-- Describe: multi-period narrative explaining changes in key metrics -->

---

## Prompt Engineering

### System Prompt

<!-- Describe financial domain instructions: accuracy requirements, citation format, no speculation guidelines -->

### Output Schema

<!-- Describe structured JSON output: summary string, key_points[], risk_flags[], confidence_score -->

```json
{
  "summary": "...",
  "key_points": ["...", "..."],
  "risk_flags": ["..."],
  "confidence": 0.87,
  "sources": [{ "filing_id": 42, "chunk_index": 7 }]
}
```

---

## Model Selection

| Use Case | Model | Reason |
|---|---|---|
| Short summaries | GPT-4o-mini | Low cost, fast |
| Deep analysis | GPT-4o / Claude Sonnet | Higher accuracy |
| Embeddings | text-embedding-3-small | Best cost/quality ratio |

---

## Cost Management

<!-- Describe token budgeting, context truncation strategy, caching repeated prompts via Redis -->

---

## Observability

<!-- Describe Langfuse trace integration: prompt version, token counts, latency, feedback scoring -->
