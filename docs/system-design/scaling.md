# Scaling

!!! info "Planned Architecture (Future Phases)"
    Production scaling infrastructure is implemented in **Phase 6** (Weeks 21–24).

---

## Overview

<!-- Describe the scaling philosophy: horizontal scale for stateless API, read replicas for DB, caching for hot paths -->

---

## API Layer Scaling

### Horizontal Scaling

<!-- Describe stateless FastAPI instances behind a load balancer, session state in Redis -->

### Rate Limiting

<!-- Describe Redis-backed rate limiting: token bucket algorithm, per-user and per-IP limits -->

---

## Database Scaling

### Read Replicas

<!-- Describe PostgreSQL read replica setup for heavy analytical queries -->

### Connection Pooling

<!-- Describe PgBouncer configuration, max connections, pool sizing formula -->

### Query Optimization

<!-- Describe index strategy, EXPLAIN ANALYZE workflow, slow query logging -->

---

## Caching Strategy

| Cache Layer | Tool | TTL | Purpose |
|---|---|---|---|
| Financial data | Redis | 24h | Reduce DB reads for stable data |
| LLM responses | Redis | 1h | Cache repeated AI analysis calls |
| Search results | Redis | 15m | Avoid redundant vector queries |

---

## Scraping Scaling

<!-- Describe parallel scraper workers, domain rate limiting to avoid bans, proxy rotation (if needed) -->

---

## LLM Cost Scaling

<!-- Describe prompt caching, response caching, model tier selection based on query complexity -->
