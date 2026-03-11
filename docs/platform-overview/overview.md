# Platform Overview

!!! success "Current MVP"
    The MVP focuses on PDF scraping, ETL, database storage, and a basic REST API with a Next.js landing page deployed on Vercel.

---

## What FinSight API Does

<!-- Describe the end-to-end flow: scrape → parse → store → expose via API → visualize → AI analysis -->

---

## Target Users

### Free Tier

<!-- Describe free-tier access: public landing page, high-level visualizations, basic company metrics -->

### Paid Tier

<!-- Describe paid-tier access: detailed dashboards, AI chatbot, developer API for algorithmic traders -->

---

## Covered Companies (MVP)

<!-- List the eight Malaysian Blue-Chip targets: Maybank, CIMB, TNB, Petronas, Maxis, Telekom, Genting, Sunway -->

| Company | Exchange | Report Type |
|---|---|---|
| Maybank | Bursa Malaysia | Quarterly / Annual |
| CIMB | Bursa Malaysia | Quarterly / Annual |
| TNB | Bursa Malaysia | Quarterly / Annual |
| Petronas | Bursa Malaysia | Annual |
| Maxis | Bursa Malaysia | Quarterly / Annual |
| Telekom Malaysia | Bursa Malaysia | Quarterly / Annual |
| Genting | Bursa Malaysia | Quarterly / Annual |
| Sunway | Bursa Malaysia | Quarterly / Annual |

---

## Monetization Strategy

<!-- Detail freemium model: free general display, paid deep-dive and API access -->

---

## Six-Month Roadmap

!!! info "Planned Architecture (Future Phases)"
    Phases 3–6 are planned and not yet implemented.

```mermaid
gantt
    title FinSight API — 6-Month Roadmap
    dateFormat  YYYY-MM-DD
    section Phase 1
    MVP & Data Acquisition       :done, p1, 2026-01-01, 3w
    section Phase 2
    ETL Pipeline & Database      :done, p2, after p1, 4w
    section Phase 3
    RAG & Backend API            :active, p3, after p2, 4w
    section Phase 4
    Dashboard & Auth             :p4, after p3, 5w
    section Phase 5
    Agentic Workflows            :p5, after p4, 3w
    section Phase 6
    MLOps & CI/CD                :p6, after p5, 4w
```

---

## Key Design Principles

<!-- Document architectural decisions: AI-native development, production-grade security, monetization-first -->
