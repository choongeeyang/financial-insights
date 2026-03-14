import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Proxy /api/* calls to the FastAPI backend during development and production
  async rewrites() {
    return [];
  },
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000",
  },
};

export default nextConfig;
