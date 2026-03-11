# API Overview

!!! success "Current MVP"
    The core financial data REST API with versioned endpoints is implemented in Phase 3.

---

## Base URL

```
https://api.finsight.dev/v1
```

---

## API Design Principles

<!-- Describe REST conventions: resource naming, versioning strategy, pagination, filtering, sorting -->

---

## Rate Limits

| Tier | Requests / Minute | Requests / Day |
|---|---|---|
| Free | 10 | 100 |
| Paid | 300 | 50,000 |
| Internal | Unlimited | Unlimited |

!!! info "Planned Architecture (Future Phases)"
    Rate limiting via Redis is implemented in Phase 6.

---

## Response Format

All API responses follow this envelope structure:

```json
{
  "success": true,
  "data": {},
  "meta": {
    "request_id": "abc123",
    "timestamp": "2026-01-01T00:00:00Z",
    "version": "v1"
  },
  "error": null
}
```

---

## Error Codes

| HTTP Status | Code | Description |
|---|---|---|
| 400 | INVALID_PARAMS | Request parameters failed validation |
| 401 | UNAUTHORIZED | Missing or invalid API key |
| 403 | FORBIDDEN | Plan does not include this resource |
| 404 | NOT_FOUND | Resource does not exist |
| 429 | RATE_LIMITED | Request quota exceeded |
| 500 | INTERNAL_ERROR | Unexpected server error |

---

## Versioning

<!-- Describe API versioning strategy: URL path versioning (v1, v2), deprecation policy, changelog -->

---

## OpenAPI / Swagger

<!-- Describe auto-generated OpenAPI docs available at /docs and /redoc -->
