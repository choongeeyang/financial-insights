# Data Quality

!!! success "Current MVP"
    Basic data validation rules are in place from Phase 2. Automated quality monitoring is planned for Phase 6.

---

## Overview

<!-- Describe why data quality is critical for a financial platform: wrong numbers erode trust -->

---

## Validation Rules

### Schema Validation

<!-- Describe Pydantic model validation on all parsed financial data before DB insert -->

```python
class IncomeStatementRow(BaseModel):
    revenue: Decimal = Field(gt=0)
    gross_profit: Decimal
    net_income: Decimal
    period: str = Field(pattern=r"Q[1-4]-\d{4}|FY\d{4}")
```

### Business Logic Validation

<!-- Describe financial sanity checks: gross_profit <= revenue, total_assets = total_liabilities + equity -->

### Cross-Period Consistency

<!-- Describe checks for anomalous period-over-period changes (e.g. >500% revenue jump flags for review) -->

---

## Quality Monitoring

!!! info "Planned Architecture (Future Phases)"
    Automated quality dashboards are planned for Phase 6.

<!-- Describe metrics tracked: completeness rate per company/period, validation failure rate, null rates per column -->

---

## Dead Letter Handling

<!-- Describe how failed records are stored: dead_letter_queue table, manual review workflow, re-processing -->

---

## Source Traceability

<!-- Describe how every database row traces to: source PDF path, parsing run ID, transformation version -->

---

## Data Freshness

<!-- Describe freshness SLAs: filings ingested within 24h of Bursa Malaysia disclosure -->
