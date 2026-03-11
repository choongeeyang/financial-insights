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
├── app/
│   ├── (public)/
│   │   ├── page.tsx              # Landing page
│   │   └── companies/[id]/       # Public company profile
│   ├── (dashboard)/
│   │   ├── layout.tsx            # Auth-gated layout
│   │   ├── overview/             # Dashboard home
│   │   ├── financials/[id]/      # Financial statement views
│   │   └── chat/                 # AI chat interface
│   └── api/                      # Next.js route handlers (BFF)
├── components/
│   ├── charts/                   # Recharts wrappers
│   ├── tables/                   # Financial data tables
│   ├── ui/                       # Shared UI primitives
│   └── layout/                   # Header, Sidebar, Footer
├── hooks/                        # Custom React hooks
├── stores/                       # Zustand stores
├── lib/                          # API client, utilities
└── types/                        # TypeScript interfaces
```

---

## Rendering Strategy

| Route | Strategy | Reason |
|---|---|---|
| Landing page | SSG | Static content, fast CDN |
| Company profiles (public) | ISR | Refreshes on new filing |
| Dashboard (paid) | CSR | Auth-gated, dynamic data |
| AI chat | CSR | Real-time streaming responses |

---

## Deployment

<!-- Describe Vercel deployment: environment variables, preview deployments, production domain -->

---

## Authentication Flow

!!! info "Planned Architecture (Future Phases)"
    Full auth integration with RBAC is implemented in Phase 4.

<!-- Describe NextAuth / Auth0 integration, protected route middleware, session cookie handling -->
