# Environment Setup

!!! success "Current MVP"
    Local development environment setup covers the backend, data pipeline, and Next.js frontend.

---

## Prerequisites

| Tool | Version | Purpose |
|---|---|---|
| Python | ≥ 3.12 | Backend and data pipeline |
| Node.js | ≥ 20 | Next.js frontend |
| Docker Desktop | Latest | All services via Compose |
| uv | Latest | Fast Python package management |
| Git | Latest | Version control |

---

## Clone the Repository

```bash
git clone https://github.com/ONGKOKRHUI/financial-insights.git
cd financial-insights
```

---

## Environment Variables

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

```bash
# .env — required variables
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/finsight
REDIS_URL=redis://localhost:6379
OPENAI_API_KEY=sk-...
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
SECRET_KEY=your-jwt-secret
```

---

## Backend Setup

```bash
cd backend
uv sync
uv run alembic upgrade head   # Run database migrations
```

---

## Frontend Setup

```bash
cd frontend
npm install
cp .env.local.example .env.local
```

---

## Docker Services

Start all infrastructure services (PostgreSQL, Redis, Elasticsearch):

```bash
docker compose up -d postgres redis elasticsearch
```

---

## pgvector Extension

```bash
# Ensure pgvector is enabled
docker compose exec postgres psql -U postgres -d finsight -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

---

## Verify Setup

```bash
# Check backend health
curl http://localhost:8000/health

# Check frontend
open http://localhost:3000
```
