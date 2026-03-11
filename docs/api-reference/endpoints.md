# Endpoints

!!! success "Current MVP"
    Financial data and company endpoints are available from Phase 3. Search and AI endpoints are Phase 3–5.

---

## Companies

### `GET /v1/companies`

List all tracked companies.

**Query Parameters**

| Parameter | Type | Description |
|---|---|---|
| `sector` | string | Filter by sector |
| `limit` | int | Max results (default: 20) |
| `offset` | int | Pagination offset |

**Response**

```json
{
  "success": true,
  "data": [
    { "id": 1, "name": "Maybank", "ticker": "1155", "sector": "Banking" }
  ]
}
```

---

### `GET /v1/companies/{id}`

Get a single company profile.

<!-- Describe response fields: name, ticker, exchange, sector, listing_date, description -->

---

## Financial Statements

### `GET /v1/companies/{id}/income-statement`

| Parameter | Type | Description |
|---|---|---|
| `period` | string | e.g. `Q3-2025`, `FY2024` |

<!-- Describe response: all income statement line items with period metadata -->

---

### `GET /v1/companies/{id}/balance-sheet`

<!-- Describe balance sheet endpoint -->

---

### `GET /v1/companies/{id}/cash-flow`

<!-- Describe cash flow endpoint -->

---

### `GET /v1/companies/{id}/ratios`

<!-- Describe financial ratios endpoint: P/E, ROE, debt-to-equity, current ratio -->

---

## Search

!!! info "Planned Architecture (Future Phases)"
    Hybrid semantic search is implemented in Phase 3.

### `POST /v1/search`

```json
{
  "query": "Maybank net interest margin 2024",
  "company_ids": [1, 2],
  "top_k": 5
}
```

<!-- Describe response: ranked document chunks with scores, source filing metadata -->

---

## AI Analysis

!!! info "Planned Architecture (Future Phases)"
    AI analysis endpoints are implemented in Phase 3 and extended in Phase 5.

### `POST /v1/ai/summarize`

<!-- Describe LLM summary generation: company_id, period, summary_type (brief/detailed) -->

### `POST /v1/ai/compare`

<!-- Describe multi-company comparison: company_ids[], period, metrics[] -->

### `POST /v1/ai/chat`

<!-- Describe chat endpoint for the agentic system: message, session_id, context -->
