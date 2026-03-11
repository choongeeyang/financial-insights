# Reliability

!!! info "Planned Architecture (Future Phases)"
    Production reliability hardening is planned for **Phase 6** (Weeks 21–24).

---

## Overview

<!-- Describe the reliability goals: uptime SLA, data freshness SLA, RTO/RPO targets -->

---

## SLA Targets

| Service | Availability Target | Notes |
|---|---|---|
| API (paid tier) | 99.9% | ~8.7 hours downtime/year |
| Scraping pipeline | 99% | Failure tolerated, data eventually consistent |
| AI endpoints | 99% | Degraded mode without AI on LLM provider outage |

---

## Health Checks

<!-- Describe /health and /ready endpoints, what each checks (DB, Redis, Elasticsearch) -->

---

## Circuit Breakers

<!-- Describe circuit breaker pattern for LLM API calls: open after N failures, half-open probe, close on recovery -->

---

## Retry Strategy

<!-- Describe exponential backoff with jitter for external API calls (LLM, scraping targets) -->

---

## Graceful Degradation

<!-- Describe how the platform behaves when AI endpoints are unavailable: serve cached responses, show stale indicator -->

---

## Backup and Recovery

<!-- Describe PostgreSQL backup schedule: daily snapshots, WAL archiving, point-in-time recovery -->

---

## Incident Response

<!-- Describe on-call rotation (future), runbook links, severity classification -->
