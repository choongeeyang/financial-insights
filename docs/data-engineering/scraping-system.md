# Scraping System

!!! success "Current MVP"
    Automated PDF download scripts for the eight target Malaysian Blue-Chip companies are implemented in Phase 1.

---

## Overview

<!-- Describe the scraping system's role: monitor Bursa Malaysia disclosure portals, detect new filings, and download PDFs -->

---

## Target Sources

| Company | Source URL | Report Types |
|---|---|---|
| Maybank | bursamalaysia.com | Quarterly, Annual |
| CIMB | bursamalaysia.com | Quarterly, Annual |
| TNB | bursamalaysia.com | Quarterly, Annual |
| Petronas | bursamalaysia.com | Annual |
| Maxis | bursamalaysia.com | Quarterly, Annual |
| Telekom Malaysia | bursamalaysia.com | Quarterly, Annual |
| Genting | bursamalaysia.com | Quarterly, Annual |
| Sunway | bursamalaysia.com | Quarterly, Annual |

---

## Technology

### Playwright

<!-- Describe dynamic page navigation, headless browser configuration, screenshot debugging -->

### Selenium (Fallback)

<!-- Describe fallback usage for legacy portals or JavaScript-heavy pages -->

---

## Scraping Logic

### Detection

<!-- Describe how new filings are detected: polling interval, diff against known filings, date filtering -->

### Download

<!-- Describe PDF download flow: auth handling, redirect following, file naming convention -->

### Storage

<!-- Describe raw PDF storage: local filesystem structure, future S3/blob migration path -->

---

## Scheduling

<!-- Describe cron schedule, Airflow/Prefect DAG trigger, manual re-run support -->

---

## Error Handling

<!-- Describe retry logic, stale file detection, alerting on consecutive failures -->

---

## Configuration

```python
# Example scraper configuration structure
SCRAPER_CONFIG = {
    "targets": [...],
    "schedule": "0 8 * * *",   # Daily at 08:00
    "retry_attempts": 3,
    "output_dir": "data/raw/pdfs/",
}
```
