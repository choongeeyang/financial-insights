# Usage Examples

!!! success "Current MVP"
    These examples work against the Phase 3 API.

---

## Quick Start

=== "curl"
    ```bash
    export FINSIGHT_API_KEY="your_api_key_here"

    curl -H "X-API-Key: $FINSIGHT_API_KEY" \
         "https://api.finsight.dev/v1/companies"
    ```

=== "Python"
    ```python
    import httpx

    client = httpx.Client(headers={"X-API-Key": "your_api_key_here"})
    response = client.get("https://api.finsight.dev/v1/companies")
    companies = response.json()["data"]
    ```

=== "JavaScript"
    ```javascript
    const res = await fetch("https://api.finsight.dev/v1/companies", {
      headers: { "X-API-Key": "your_api_key_here" },
    });
    const { data: companies } = await res.json();
    ```

---

## Fetch an Income Statement

=== "curl"
    ```bash
    curl -H "X-API-Key: $FINSIGHT_API_KEY" \
         "https://api.finsight.dev/v1/companies/1/income-statement?period=Q3-2025"
    ```

=== "Python"
    ```python
    response = client.get(
        "https://api.finsight.dev/v1/companies/1/income-statement",
        params={"period": "Q3-2025"},
    )
    statement = response.json()["data"]
    print(statement["net_income"])
    ```

---

## Semantic Search

!!! info "Planned Architecture (Future Phases)"
    Available from Phase 3.

=== "Python"
    ```python
    response = client.post(
        "https://api.finsight.dev/v1/search",
        json={
            "query": "Maybank net interest margin trends",
            "company_ids": [1],
            "top_k": 5,
        },
    )
    results = response.json()["data"]
    for chunk in results:
        print(chunk["content"], chunk["score"])
    ```

---

## AI Company Summary

!!! info "Planned Architecture (Future Phases)"
    Available from Phase 3.

=== "Python"
    ```python
    response = client.post(
        "https://api.finsight.dev/v1/ai/summarize",
        json={
            "company_id": 1,
            "period": "FY2024",
            "summary_type": "detailed",
        },
    )
    print(response.json()["data"]["summary"])
    ```

---

## SDK (Planned)

!!! info "Planned Architecture (Future Phases)"
    Official Python and JavaScript SDKs are planned for Phase 4+.

<!-- Describe planned SDK: pip install finsight, npm install @finsight/sdk -->
