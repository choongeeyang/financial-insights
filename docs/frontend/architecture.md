# Frontend Architecture

!!! success "Current MVP"
    The Next.js application with landing page, basic company pages, and Vercel deployment is live from Phase 1.

---

## Tech Stack

| Library | Purpose |
|---|---|
| Next.js (App Router) | React framework, SSR / SSG |
| TypeScript | Type safety |
| Zustand | Client-side state management |
| TanStack Query | Server state, caching, and data fetching |
| Recharts / Chart.js | Financial chart visualizations |
| Tailwind CSS | Utility-first styling |

---

## Project Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── page.tsx                      # Landing page (SSG)
│   │   ├── layout.tsx                    # Root layout with Header + Footer
│   │   ├── not-found.tsx                 # 404 page
│   │   ├── companies/
│   │   │   ├── page.tsx                  # Company listing (SSG)
│   │   │   └── [id]/page.tsx             # Company profile (ISR)
│   │   └── api/                          # Next.js BFF route handlers
│   │       ├── companies/route.ts        # GET /api/companies
│   │       ├── companies/[id]/route.ts   # GET /api/companies/{ticker}
│   │       └── financials/[id]/route.ts  # GET /api/financials/{ticker}
│   ├── components/
│   │   ├── charts/
│   │   │   ├── RevenueTrendChart.tsx     # Recharts LineChart — revenue & net income
│   │   │   ├── IncomeBarChart.tsx        # Recharts BarChart — income breakdown
│   │   │   └── MarginChart.tsx           # Recharts AreaChart — profitability margins
│   │   ├── tables/
│   │   │   └── FinancialsTable.tsx       # Annual income statement with YoY deltas
│   │   ├── ui/
│   │   │   ├── KPICard.tsx               # Metric card with value, YoY delta, subtitle
│   │   │   ├── CompanyCard.tsx           # Linked company tile for listings
│   │   │   ├── Skeleton.tsx              # Loading skeleton variants
│   │   │   └── Badge.tsx                 # Status / sector badge
│   │   └── layout/
│   │       ├── Header.tsx                # Sticky nav with search input
│   │       └── Footer.tsx                # Site footer
│   ├── hooks/
│   │   ├── useCompanies.ts               # TanStack Query hooks for company data
│   │   └── useFinancials.ts              # TanStack Query hook for income statement
│   ├── stores/
│   │   └── searchStore.ts                # Zustand store for ticker search state
│   ├── lib/
│   │   ├── api.ts                        # API client targeting BFF routes
│   │   ├── utils.ts                      # Formatters, color helpers, YoY calc
│   │   └── providers.tsx                 # TanStack QueryClientProvider wrapper
│   └── types/
│       └── index.ts                      # TypeScript interfaces for all API shapes
├── vercel.json                           # Vercel deployment config
├── next.config.ts                        # Next.js config with env vars
└── .env.example                          # Required environment variables
```

---

## Rendering Strategy

| Route | Strategy | Reason |
|---|---|---|
| Landing page (`/`) | SSG | Static content, fast CDN |
| Company listing (`/companies`) | SSG | Infrequently changing list |
| Company profiles (`/companies/[id]`) | ISR (1 hr) | Refreshes on new filing |
| Dashboard (paid) | CSR | Auth-gated, dynamic data (Phase 4) |
| AI chat | CSR | Real-time streaming responses (Phase 5) |

---

## Deployment

### Frontend → Vercel

The frontend is deployed to Vercel via GitHub Actions on every push to `main` that touches `frontend/**`.

**Workflow:** `.github/workflows/deploy-frontend.yml`

1. Runs `npm ci` and `npx tsc --noEmit` for type checking.
2. Runs `npm run build` with environment variable injection.
3. Deploys to production using `amondnet/vercel-action@v25`.

**Required GitHub Secrets:**

| Secret | Description |
|---|---|
| `VERCEL_TOKEN` | Vercel personal access token |
| `VERCEL_ORG_ID` | Vercel team/org ID |
| `VERCEL_PROJECT_ID` | Vercel project ID |
| `NEXT_PUBLIC_API_URL` | Public FastAPI URL (e.g. `https://finsight-api.onrender.com`) |
| `INTERNAL_API_URL` | Server-side FastAPI URL (same as above on Vercel) |

**Setup steps:**

1. Create a Vercel project and link it to the `financial-insights` repository with `Root Directory: frontend`.
2. Retrieve `VERCEL_ORG_ID` and `VERCEL_PROJECT_ID` from `.vercel/project.json` after running `vercel link`.
3. Generate a `VERCEL_TOKEN` from [vercel.com/account/tokens](https://vercel.com/account/tokens).
4. Add all secrets to the GitHub repository under **Settings → Secrets and variables → Actions**.

### Backend → Render

The FastAPI backend is deployed to Render via a deploy hook triggered by GitHub Actions.

**Workflow:** `.github/workflows/deploy-backend.yml`

1. Validates Python imports (`from backend.main import app`).
2. Triggers the Render deploy hook via `curl`.

**Required GitHub Secret:**

| Secret | Description |
|---|---|
| `RENDER_DEPLOY_HOOK_URL` | Deploy hook URL from Render dashboard |

**Setup steps:**

1. Create a new Web Service on [render.com](https://render.com) pointing to this repository.
2. Set `Root Directory: .` and `Start Command: uvicorn backend.main:app --host 0.0.0.0 --port $PORT`.
3. Copy the deploy hook URL from the service's **Settings → Deploy Hook**.
4. Add it as `RENDER_DEPLOY_HOOK_URL` in GitHub secrets.
5. Set `ALLOWED_ORIGINS` environment variable on Render to the Vercel production URL.

---

## Authentication Flow

!!! info "Planned Architecture (Future Phases)"
    Full auth integration with RBAC is implemented in Phase 4.

Full auth integration using OAuth2 / JWT with HttpOnly cookies is planned for Phase 4. In Phase 1, all routes are public.
