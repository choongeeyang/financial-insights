# State Management

!!! success "Current MVP"
    Basic TanStack Query data fetching is available from Phase 1. Zustand stores and RBAC-aware state are added in Phase 4.

---

## State Architecture

FinSight separates state into two categories:

| Type | Tool | Examples |
|---|---|---|
| **Server state** | TanStack Query | Financial data, company lists, AI responses |
| **Client state** | Zustand | Selected company, active period, UI preferences |

---

## TanStack Query

### Query Keys

```typescript
export const queryKeys = {
  companies: () => ["companies"] as const,
  company: (id: number) => ["companies", id] as const,
  incomeStatement: (id: number, period: string) =>
    ["companies", id, "income-statement", period] as const,
  aiSummary: (id: number, period: string) =>
    ["ai", "summary", id, period] as const,
};
```

### Caching Strategy

<!-- Describe staleTime and gcTime configuration per query type -->

### Optimistic Updates

<!-- Describe optimistic update pattern for any write operations (e.g. user preferences) -->

---

## Zustand Stores

### `useFinancialStore`

```typescript
interface FinancialStore {
  selectedCompanyId: number | null;
  activePeriod: string;
  setSelectedCompany: (id: number) => void;
  setActivePeriod: (period: string) => void;
}
```

### `useAuthStore`

!!! info "Planned Architecture (Future Phases)"
    Auth store with RBAC is implemented in Phase 4.

<!-- Describe auth store: user object, tier, permissions, hydration from session -->

### `uiStore`

<!-- Describe UI preferences: sidebar collapsed state, theme override, table vs chart view -->

---

## Data Fetching Patterns

### Financial Statements with Suspense

<!-- Describe React Suspense + TanStack Query pattern for financial data pages -->

### Streaming AI Responses

<!-- Describe EventSource / fetch streaming pattern for AI chat messages -->
