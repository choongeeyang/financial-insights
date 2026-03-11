# Services

!!! success "Current MVP"
    Core services for financial data retrieval and company lookups are implemented in Phase 3.

---

## Service Layer Design

<!-- Describe why business logic lives in a service layer separate from routers -->

---

## FinancialService

<!-- Describe methods: get_income_statement, get_balance_sheet, get_cash_flow, get_key_ratios -->

```python
class FinancialService:
    async def get_income_statement(
        self, company_id: int, period: str
    ) -> IncomeStatement: ...

    async def get_key_ratios(
        self, company_id: int, periods: list[str]
    ) -> list[FinancialRatio]: ...
```

---

## CompanyService

<!-- Describe methods: list_companies, get_company_profile, get_filing_history -->

---

## SearchService

!!! info "Planned Architecture (Future Phases)"
    Hybrid search combining pgvector and Elasticsearch is implemented in Phase 3.

<!-- Describe hybrid_search method: query encoding, dual retrieval, RRF fusion -->

---

## AIAnalysisService

!!! info "Planned Architecture (Future Phases)"
    LLM-powered analysis service is implemented in Phase 3.

<!-- Describe methods: generate_summary, compare_companies, answer_question -->

---

## CacheService

!!! info "Planned Architecture (Future Phases)"
    Redis caching layer is implemented in Phase 6.

<!-- Describe cache key strategy, TTL values per data type, cache invalidation on new filings -->
