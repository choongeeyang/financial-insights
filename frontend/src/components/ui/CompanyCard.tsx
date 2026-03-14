import Link from "next/link"; // Next.js Link for client-side navigation
import { formatBillions, sectorBadgeClass } from "@/lib/utils"; // Utility functions
import type { CompanySummary } from "@/types"; // Type definition for company data

// Props interface for the CompanyCard component
interface CompanyCardProps {
  company: CompanySummary; // company object containing summary info
}

/**
 * CompanyCard Component
 * --------------------
 * Displays a clickable summary card for a company, including:
 * - Ticker symbol
 * - Company name
 * - Sector badge
 * - Market capitalization
 *
 * Clicking the card navigates to the company's detail page.
 */
export default function CompanyCard({ company }: CompanyCardProps) {
  return (
    // Wrap the card in a Next.js Link to navigate to `/companies/[ticker]`
    <Link href={`/companies/${company.ticker}`}>
      {/* Card container with rounded corners, border, background, and hover effects */}
      <div className="group rounded-xl border border-slate-200 bg-white p-5 hover:border-blue-300 hover:shadow-md transition-all duration-200">
        
        {/* Header: Ticker and company name */}
        <div className="flex items-start justify-between">
          <div>
            {/* Ticker badge */}
            <span className="inline-block rounded-md bg-slate-100 px-2 py-0.5 text-xs font-bold text-slate-700 font-mono">
              {company.ticker}
            </span>

            {/* Company name */}
            <h3 className="mt-2 text-sm font-semibold text-slate-900 group-hover:text-blue-600 transition-colors leading-tight">
              {company.name}
            </h3>
          </div>
        </div>

        {/* Footer: Sector and Market Capitalization */}
        <div className="mt-3 flex items-center justify-between">
          {/* Sector badge with dynamic styling based on sector */}
          <span
            className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${sectorBadgeClass(
              company.sector
            )}`}
          >
            {company.sector}
          </span>

          {/* Market capitalization formatted in billions with currency */}
          <span className="text-sm font-semibold text-slate-700">
            {formatBillions(company.market_cap_bln, company.currency)}
          </span>
        </div>
      </div>
    </Link>
  );
}