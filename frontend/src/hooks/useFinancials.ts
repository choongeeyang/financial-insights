"use client";

import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api";

export function useIncomeStatement(ticker: string) {
  return useQuery({
    queryKey: ["income-statement", ticker],
    queryFn: () => api.financials.incomeStatement(ticker),
    staleTime: 10 * 60 * 1000,
    enabled: !!ticker,
  });
}
