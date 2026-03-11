# Database Schema

!!! success "Current MVP"
    The core PostgreSQL schema for companies, filings, and financial statements is designed and migrated in Phase 2.

---

## Entity Relationship Overview

```mermaid
erDiagram
    COMPANIES {
        int id PK
        string name
        string ticker
        string exchange
        string sector
    }
    FILINGS {
        int id PK
        int company_id FK
        string report_type
        string period
        date filing_date
        string source_url
        string pdf_path
    }
    INCOME_STATEMENTS {
        int id PK
        int filing_id FK
        decimal revenue
        decimal gross_profit
        decimal operating_income
        decimal net_income
        decimal eps
    }
    BALANCE_SHEETS {
        int id PK
        int filing_id FK
        decimal total_assets
        decimal total_liabilities
        decimal total_equity
        decimal cash_and_equivalents
    }
    CASH_FLOWS {
        int id PK
        int filing_id FK
        decimal operating_cf
        decimal investing_cf
        decimal financing_cf
        decimal free_cash_flow
    }
    DOCUMENT_CHUNKS {
        int id PK
        int filing_id FK
        text content
        int chunk_index
        vector embedding
    }
    USERS {
        int id PK
        string email
        string hashed_password
        string tier
        datetime created_at
    }

    COMPANIES ||--o{ FILINGS : has
    FILINGS ||--o| INCOME_STATEMENTS : contains
    FILINGS ||--o| BALANCE_SHEETS : contains
    FILINGS ||--o| CASH_FLOWS : contains
    FILINGS ||--o{ DOCUMENT_CHUNKS : split_into
```

---

## Tables

### `companies`

<!-- Describe columns, indexes, and constraints -->

### `filings`

<!-- Describe columns, compound unique index on (company_id, period, report_type), soft-delete flag -->

### `income_statements`

<!-- Describe all financial line items stored, units (MYR thousands), null handling -->

### `balance_sheets`

<!-- Describe all balance sheet line items -->

### `cash_flows`

<!-- Describe cash flow statement line items -->

### `document_chunks`

<!-- Describe pgvector column type: vector(1536), HNSW index configuration -->

### `users`

!!! info "Planned Architecture (Future Phases)"
    User auth tables are added in Phase 4.

<!-- Describe user table, tier enum (free/paid), API key storage -->

---

## Migrations

<!-- Describe Alembic setup, naming convention for migration files, rollback strategy -->

---

## pgvector Setup

<!-- Describe extension installation, index type (HNSW vs IVFFlat), distance function (cosine) -->

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE INDEX ON document_chunks
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);
```
