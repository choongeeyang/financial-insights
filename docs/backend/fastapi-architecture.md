# FastAPI Architecture

!!! success "Current MVP"
    The core FastAPI application with routing, middleware, and dependency injection is implemented in Phase 3.

---

## Project Structure

```
backend/
├── app/
│   ├── main.py               # Application entry point
│   ├── config.py             # Settings via pydantic-settings
│   ├── dependencies.py       # Shared DI: DB session, auth user
│   ├── routers/
│   │   ├── financials.py     # Financial data endpoints
│   │   ├── companies.py      # Company profile endpoints
│   │   ├── search.py         # Hybrid search endpoints
│   │   ├── ai.py             # AI analysis endpoints
│   │   └── auth.py           # Authentication endpoints
│   ├── services/             # Business logic layer
│   ├── models/               # SQLAlchemy ORM models
│   ├── schemas/              # Pydantic request/response schemas
│   └── core/
│       ├── security.py       # JWT / OAuth2 helpers
│       └── database.py       # Async DB engine setup
├── tests/
├── Dockerfile
└── pyproject.toml
```

---

## Application Lifecycle

<!-- Describe startup/shutdown events: DB connection pool init, Elasticsearch client init, Redis connection -->

---

## Middleware Stack

| Middleware | Purpose |
|---|---|
| CORS | Allow cross-origin requests from Next.js |
| Rate Limiter | Redis-backed per-user/IP request throttling |
| Request Logger | Structured logging for all inbound requests |
| Auth | JWT validation on protected routes |

---

## Dependency Injection

<!-- Describe the shared DI factories: get_db, get_current_user, get_redis_client -->

---

## Error Handling

<!-- Describe global exception handlers, error response schema, HTTP status code conventions -->

---

## Configuration

<!-- Describe pydantic-settings config: DATABASE_URL, REDIS_URL, SECRET_KEY, LLM_API_KEY, environment flags -->
