# Agentic System

!!! info "Planned Architecture (Future Phases)"
    The multi-agent system is implemented in **Phase 5** (Weeks 17–19).

---

## Overview

<!-- Describe the shift from simple LLM calls to a multi-agent architecture: dynamic tool routing, session memory, autonomous decision-making -->

---

## LangGraph Architecture

### Graph Definition

```python
from langgraph.graph import StateGraph

workflow = StateGraph(AgentState)
workflow.add_node("supervisor", supervisor_agent)
workflow.add_node("rag_agent", rag_agent)
workflow.add_node("sql_agent", sql_agent)
workflow.add_node("analysis_agent", analysis_agent)
workflow.add_node("formatter", response_formatter)
```

### Routing Logic

<!-- Describe how the supervisor classifies intent and routes to the appropriate agent -->

---

## Agents

### Supervisor Agent

<!-- Describe: intent classification, routing decision, fallback to clarifying question -->

### RAG Agent

<!-- Describe: invokes the RAG pipeline with the user query, passes retrieved context to formatter -->

### SQL Agent

<!-- Describe: converts natural language to PostgreSQL query, executes safely, formats results -->

### Analysis Agent

<!-- Describe: multi-document reasoning, trend interpretation, sector comparison -->

---

## MCP Tools

<!-- Describe the Model Context Protocol tool implementations exposed to agents -->

| Tool Name | Description |
|---|---|
| `search_reports` | Semantic search over financial document chunks |
| `query_financials` | Structured SQL query against financial tables |
| `get_company_profile` | Fetch company metadata and latest filing info |
| `get_financial_ratios` | Compute and return financial ratios for a period |

---

## Session Memory

<!-- Describe conversation history management: LangGraph checkpoints, turn-level context window -->

---

## Observability with Langfuse

<!-- Describe per-turn tracing: agent selected, tool called, tokens used, latency, cost per session -->

---

## Guardrails

<!-- Describe safety measures: SQL injection prevention, hallucination reduction, unsupported query rejection -->
