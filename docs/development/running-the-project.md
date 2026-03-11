# Running the Project

!!! success "Current MVP"
    All commands below work against the current MVP stack.

---

## Start All Services

```bash
docker compose up -d
```

This starts: PostgreSQL, Redis, Airflow (or Prefect), Elasticsearch.

---

## Run the Backend

```bash
cd backend
uv run fastapi dev app/main.py --port 8000
```

The API will be available at:

- **API:** `http://localhost:8000`
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## Run the Frontend

```bash
cd frontend
npm run dev
```

The dashboard will be available at `http://localhost:3000`.

---

## Run the Scraper (Manual Trigger)

```bash
cd pipeline
uv run python scraper/run.py --company maybank --period Q3-2025
```

---

## Run the ETL Pipeline

```bash
# Trigger a full ETL run for a specific filing
uv run python etl/run.py --filing-id 42

# Or trigger via Airflow
airflow dags trigger finsight_etl_pipeline
```

---

## Database Migrations

```bash
cd backend

# Apply all pending migrations
uv run alembic upgrade head

# Create a new migration
uv run alembic revision --autogenerate -m "add_users_table"

# Roll back one migration
uv run alembic downgrade -1
```

---

## Running Tests

=== "Backend"
    ```bash
    cd backend
    uv run pytest tests/ -v
    ```

=== "Frontend"
    ```bash
    cd frontend
    npm run test
    npm run test:e2e
    ```

=== "Pipeline"
    ```bash
    cd pipeline
    uv run pytest tests/ -v
    ```

---

## Building the Documentation

```bash
# Install MkDocs dependencies
pip install mkdocs-material mkdocs-minify-plugin

# Serve locally with live reload
mkdocs serve

# Build static site
mkdocs build
```
