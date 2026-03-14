"use client";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { useState } from "react";

/**
 * Providers component
 * -------------------
 * Wraps the app with React Query's QueryClientProvider, 
 * allowing all child components to use React Query hooks.
 *
 * @param children - React nodes that will have access to React Query
 */
export function Providers({ children }: { children: React.ReactNode }) {
  /**
   * Create a single QueryClient instance for the app.
   * Using useState with a function ensures that the client
   * is only created once, even if the component re-renders.
   */
  const [queryClient] = useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            /**
             * staleTime: how long (in ms) a query stays "fresh"
             * before React Query automatically refetches it.
             * Here it's set to 60 seconds.
             */
            staleTime: 60 * 1000, 

            /**
             * retry: number of times to retry a failed query
             * before throwing an error. Here it's set to 1 retry.
             */
            retry: 1,
          },
        },
      })
  );

  /**
   * Return the QueryClientProvider with the shared QueryClient.
   * All child components can now use React Query hooks like useQuery
   * and useMutation.
   */
  return (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
}