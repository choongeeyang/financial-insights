# FinSight API

FinSight API is an automated platform that scrapes, parses, and analyzes financial reports from Malaysian Blue-Chip companies, transforming unstructured PDFs into structured JSON and actionable intelligence. It bridges the gap between raw financial disclosures and actionable developer tooling, surfacing data through a developer API, an interactive dashboard, and an AI-powered analysis layer.

## 🚀 Features

### For Investors & Analysts (Free Tier)
- **General Dashboard**: High-level visualizations and basic company metrics of Malaysian Blue-Chip companies (e.g., Maybank, CIMB, TNB).
- **Automated Data Pipeline**: Continuous monitoring and parsing of quarterly and yearly financial reports.
- **Cleaned Financial Data**: Structured extraction of complex financial tables from raw PDFs.

### For Algorithmic Traders & Pro Users (Paid Tier)
- **Deep Financial Analysis**: Access to a detailed dashboard with advanced visualizations and historical trends.
- **AI Chatbot Interface**: Custom queries over company financials using advanced RAG and autonomous agent workflows.
- **Developer API**: Direct access to parsed structured JSON and LLM summaries for model training and integration into trading models.
- **Multi-Agent Reasoning**: Dynamic agent skills (via MCP) to fetch from vector stores or write SQL queries against financial data.

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Next.js + React + Node.js |
| **Styling** | Tailwind CSS + Recharts / Chart.js |
| **State Management** | Zustand + TanStack Query |
| **Backend** | Python 3.12+ + FastAPI |
| **Database** | PostgreSQL + pgvector (Primary), Elasticsearch (Search), Redis (Cache/Rate Limiting) |
| **Data Engineering** | Playwright / Selenium, PyMuPDF, Airflow / Prefect |
| **AI / ML** | RAG Pipelines, LangGraph, MCP Tools, Langfuse, MLflow, PyTorch / XGBoost |
| **Infrastructure** | Docker Compose, GitHub Actions (CI/CD) |

### 🔑 Environment Variables

The project requires several environment variables to be set for full functionality.

1. **Backend Secrets**: Create a `.env` file in the **backend** directory (copied from `.env.example`).
   ```bash
   # Database (Docker Compose)
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/finsight

   # Redis
   REDIS_URL=redis://localhost:6379

   # Authentication
   SECRET_KEY=your-jwt-secret-here

   # AI / Observability
   OPENAI_API_KEY=sk-your-openai-api-key
   LANGFUSE_PUBLIC_KEY=pk-your-langfuse-public-key
   LANGFUSE_SECRET_KEY=sk-your-langfuse-secret-key
   ```

2. **Frontend Configuration**: Create a `.env.local` file in the **frontend** directory (copied from `.env.local.example`).
   ```bash
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

## ⚡ Quick Start

### Prerequisites

- Python 3.12+
- Node.js 20+
- [uv](https://github.com/astral-sh/uv) (Modern Python package manager)
- Docker Desktop
- Git

### Installation & Setup

1. **Clone the Repository**:
```bash
git clone https://github.com/ONGKOKRHUI/financial-insights.git
cd financial-insights
```

2. **Backend Setup**:
```bash
cd backend
uv sync
uv run alembic upgrade head   # Run database migrations
cd ..
```

3. **Frontend Setup**:
```bash
cd frontend
npm install
cd ..
```

4. **Launch Infrastructure (Database, Redis, Elasticsearch)**:
```bash
docker compose up -d postgres redis elasticsearch
```

5. **Ensure pgvector is enabled**:
```bash
docker compose exec postgres psql -U postgres -d finsight -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

6. **Launch Development Environment**:
Start the backend server (FastAPI) and frontend (Next.js). Check the `Makefile` or package scripts for exact commands.
*(Example commands below, adjust as needed)*
```bash
# Terminal 1: Backend
cd backend && uv run uvicorn main:app --reload

# Terminal 2: Frontend
cd frontend && npm run dev
```

### URLs

- **Frontend Dashboard**: http://localhost:3000
- **Backend API Docs (Swagger UI)**: http://localhost:8000/docs
- **Backend API Health Check**: http://localhost:8000/health

## 📂 Project Structure

```
financial-insights/
├── backend/            # FastAPI backend application & API layer
├── frontend/           # Next.js web application
├── docs/               # Technical documentation (MkDocs)
├── dev-documentation/  # Project requirements and plans
├── docker/             # Docker configurations (planned)
├── scripts/            # Scraping and pipeline scripts (planned)
└── docker-compose.yml  # Docker Compose for local infrastructure
```

## 🏗 Architecture

FinSight API follows a modern, AI-first decoupled architecture:

- **Web Scraper & ETL**: Automated data ingestion pipelines using Playwright and PyMuPDF to extract tables and text from Malaysian company reports.
- **Relational & Vector Store**: PostgreSQL with `pgvector` for raw structured data and embeddings, supplemented by Elasticsearch for hybrid search.
- **Backend**: A high-performance FastAPI service orchestrating data retrieval, RAG operations, and API endpoints.
- **Frontend**: A Next.js application consuming the API for rich data visualizations and AI chatbot interactions.
- **AI Engine**: A multi-agent system powered by LangGraph, utilizing MCP tools for reasoning over financial metrics.

For deep-dive documentation, run `mkdocs serve` in the project root or view the [Documentation site](https://ONGKOKRHUI.github.io/financial-insights).

## 🧪 Testing

Testing is implemented for both the ETL pipelines and the API backend.

```bash
# Run backend tests
cd backend && uv run pytest

# Run frontend tests
cd frontend && npm run test
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
