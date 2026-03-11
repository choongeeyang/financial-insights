# PDF Parsing

!!! success "Current MVP"
    PyMuPDF-based parsing for text extraction and financial table detection is implemented in Phase 2.

---

## Overview

<!-- Describe the parsing challenge: unstructured PDFs with varying layouts, tables, footers, and multi-column text -->

---

## Technology Stack

| Tool | Purpose |
|---|---|
| PyMuPDF (fitz) | Primary PDF text and table extraction |
| Unstructured (optional) | Complex layout parsing for non-standard reports |
| pdfplumber (optional) | Fallback for table-heavy documents |

---

## Extraction Targets

<!-- Describe what is extracted: income statement, balance sheet, cash flow statement, key ratios, notes -->

### Financial Tables

<!-- Describe table detection heuristics: bounding boxes, header rows, multi-page table merging -->

### Narrative Text

<!-- Describe text block extraction, section header detection, noise removal -->

### Metadata

<!-- Describe company name, report period, filing date extraction from PDF metadata and first pages -->

---

## Output JSON Schema

```json
{
  "company": "Maybank",
  "period": "Q3 2025",
  "filing_date": "2025-11-15",
  "tables": {
    "income_statement": {},
    "balance_sheet": {},
    "cash_flow": {}
  },
  "narrative": {
    "management_discussion": "",
    "outlook": ""
  }
}
```

---

## Quality Checks

<!-- Describe validation rules: required fields present, numeric sanity checks, row/column balance assertions -->

---

## Known Limitations

<!-- Document edge cases: scanned PDFs with no text layer, non-standard table formats, multi-language content -->
