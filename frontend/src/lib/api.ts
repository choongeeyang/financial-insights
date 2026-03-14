/**
 typed API client for frontend that:
• centralizes all API requests
• provides TypeScript safety
• handles errors
• enables caching
• simplifies React Query usage
 */

import type {
  CompanySummary,
  CompanyDetail,
  KPISummary,
  IncomeStatementResponse,
} from "@/types";

// Base path for Next.js API routes (BFF proxy to FastAPI)
const BASE = "/api";

/**
 * Generic helper to fetch JSON from the API
 */
async function fetchJSON<T>(path: string): Promise<T> {
  // Fetch data with Next.js cache revalidation (1 hour)
  const res = await fetch(`${BASE}${path}`, { next: { revalidate: 3600 } });

  // Throw error if request failed
  if (!res.ok) {
    const text = await res.text().catch(() => "Unknown error");
    throw new Error(`API error ${res.status}: ${text}`);
  }

  // Parse JSON response
  return res.json() as Promise<T>;
}

export const api = {
  // Company-related endpoints
  companies: {
    list: () => fetchJSON<CompanySummary[]>("/companies"),
    get: (ticker: string) => fetchJSON<CompanyDetail>(`/companies/${ticker}`),
    summary: (ticker: string) =>
      fetchJSON<KPISummary>(`/companies/${ticker}/summary`),
  },

  // Financial data endpoints
  financials: {
    incomeStatement: (ticker: string) =>
      fetchJSON<IncomeStatementResponse>(`/financials/${ticker}`),
  },
};