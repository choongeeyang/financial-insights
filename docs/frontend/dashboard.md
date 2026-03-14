# Dashboard

!!! info "Planned Architecture (Future Phases)"
    The full paid-tier interactive dashboard is implemented in Phase 4. A basic public landing page with company previews is live from Phase 1.

---

## Dashboard Pages

### Overview Page (Phase 1 — Live)

The public landing page (`/`) serves as the MVP overview:

- **Hero section** — gradient banner with CTA buttons linking to `/companies` and the MAYBANK demo profile.
- **Company quick-links strip** — horizontal scrollable row of all 8 ticker badges.
- **Feature highlights grid** — 4-column grid explaining the platform's data, API, charts, and coverage.
- **API preview panel** — side-by-side endpoint list and a live JSON response code block.
- **Company grid** — 2×4 grid of company tiles linking to individual profiles.

### Financial Statements Page

The company profile page (`/companies/[id]`) includes a full income statement view:

- **Breadcrumb navigation** — `Home / Companies / MAYBANK`.
- **Company header** — logo initials, full name, ticker badge, sector, industry, exchange, currency.
- **Company metadata** — founded year, headquarters, employee count, market cap in a 4-column grid.
- **Financial table** (`FinancialsTable`) — 5-year income statement in descending order with YoY delta badges.

### Trend Analysis Page

Embedded within the company profile as the "Financial Trends" section:

- **Revenue & Net Income trend** (`RevenueTrendChart`) — dual-line Recharts chart over 5 fiscal years.
- **Income breakdown** (`IncomeBarChart`) — grouped bar chart comparing gross profit, operating income, and net income.
- **Profitability margins** (`MarginChart`) — area chart showing gross, operating, and net margin percentages.

### Company Comparison Page

!!! info "Planned Architecture (Future Phases)"
    Side-by-side company comparison is planned for Phase 2 or Phase 4.

### AI Chat Page

!!! info "Planned Architecture (Future Phases)"
    AI chat interface is implemented in Phase 5.

---

## Chart Components

### Revenue Trend Chart (`RevenueTrendChart.tsx`)

- **Type:** Recharts `LineChart` with `ResponsiveContainer`
- **Data:** `IncomeStatementEntry[]` — `fiscal_year`, `revenue_bln`, `net_income_bln`
- **Lines:** Revenue (blue `#3b82f6`), Net Income (emerald `#10b981`)
- **Tooltip:** Custom styled tooltip showing `{currency} {value}B` per series
- **Axes:** Year on X-axis, billions on Y-axis with `{n}B` tick format

### Income Bar Chart (`IncomeBarChart.tsx`)

- **Type:** Recharts `BarChart` with rounded bar corners
- **Data:** `IncomeStatementEntry[]` — gross profit, operating income, net income
- **Bars:** Gross Profit (blue), Operating Income (purple), Net Income (emerald)
- **Use case:** Compare income waterfall components across fiscal years

### Margin Chart (`MarginChart.tsx`)

- **Type:** Recharts `AreaChart` with gradient fills
- **Data:** `gross_margin_pct`, `operating_margin_pct`, `net_margin_pct`
- **Fills:** Gradient overlays per margin type; percentage Y-axis

### KPI Cards (`KPICard.tsx`)

Each card displays:
- **Label** — uppercase tracked metric name (e.g. `REVENUE`, `NET INCOME`)
- **Value** — formatted string (e.g. `MYR 30.2B`, `12.4×`, `28.4%`)
- **YoY delta** — colour-coded `▲ / ▼ {pct}% YoY` badge (green positive, red negative)
- **Subtitle** — optional secondary label (e.g. fiscal year)

The Phase 1 company profile renders 8 KPI cards in a 2×4 / 4-column responsive grid.

---

## Responsive Design

- **Mobile-first breakpoints:** all grids start `grid-cols-1` and expand via `sm:`, `lg:`, `xl:` modifiers.
- **Charts:** wrapped in Recharts `ResponsiveContainer width="100%" height={240}` to fill their column.
- **Tables:** `overflow-x-auto` wrapper allows horizontal scroll on narrow viewports.
- **Header search:** input width collapses from `w-56` to `w-40` below `sm` breakpoint.

---

## Performance

- **SSG & ISR:** Company listing and profiles are pre-rendered at build time; ISR revalidates every 3600 s.
- **Server-side data fetching:** Company profile uses `Promise.all` to parallelize three backend calls.
- **TanStack Query caching:** Client-side hooks cache company and financial data for 5–10 minutes.
- **Skeleton loading states:** `KPICardSkeleton`, `ChartSkeleton`, `TableSkeleton` prevent layout shift.

---

## Access Control (RBAC)

!!! info "Planned Architecture (Future Phases)"
    Route-level access control is implemented in Phase 4.

In Phase 1, all routes are public. Phase 4 will add:

- NextAuth / Auth0 session management
- JWT with HttpOnly cookies
- Protected route middleware for `/dashboard/**`
- Plan-gated component rendering with upgrade CTA
