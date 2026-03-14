"use client";

import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api";

/**
 * Fetches the list of all companies.
 * Uses React Query to handle caching, loading states, and refetching.
 */
export function useCompanies() {
  return useQuery({
    queryKey: ["companies"], // Unique key used by React Query to cache this data
    queryFn: () => api.companies.list(), // API call that retrieves the company list
    staleTime: 5 * 60 * 1000, // Data stays fresh for 5 minutes before refetching
  });
}

/**
 * Fetches detailed information for a specific company.
 * @param ticker - Stock ticker symbol (e.g., "AAPL", "MSFT")
 */
export function useCompany(ticker: string) {
  return useQuery({
    queryKey: ["company", ticker], // Cache key includes ticker to separate each company
    queryFn: () => api.companies.get(ticker), // API call to fetch company details
    staleTime: 5 * 60 * 1000, // Cache considered fresh for 5 minutes
    enabled: !!ticker, // Only run query if ticker exists
  });
}

/**
 * Fetches a summary (e.g., financial metrics) for a specific company.
 * @param ticker - Stock ticker symbol
 */
export function useCompanySummary(ticker: string) {
  return useQuery({
    queryKey: ["company-summary", ticker], // Separate cache for company summaries
    queryFn: () => api.companies.summary(ticker), // API call to fetch summary data
    staleTime: 5 * 60 * 1000, // Data remains fresh for 5 minutes
    enabled: !!ticker, // Prevent query if ticker is empty/undefined
  });
}