import Link from "next/link";

export default function Footer() {
  return (
    <footer className="border-t border-slate-200 bg-white">
      <div className="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 gap-8 sm:grid-cols-3">
          <div>
            <div className="flex items-center gap-2 text-lg font-bold text-slate-900">
              <span className="flex h-7 w-7 items-center justify-center rounded-lg bg-blue-600 text-white text-xs font-bold">
                FS
              </span>
              FinSight
            </div>
            <p className="mt-2 text-sm text-slate-500">
              Financial data API for Malaysian Blue-Chip companies. Built for developers and analysts.
            </p>
          </div>

          <div>
            <h3 className="text-sm font-semibold text-slate-900">Platform</h3>
            <ul className="mt-3 space-y-2 text-sm text-slate-500">
              <li><Link href="/" className="hover:text-slate-900 transition-colors">Home</Link></li>
              <li><Link href="/companies" className="hover:text-slate-900 transition-colors">Companies</Link></li>
            </ul>
          </div>

          <div>
            <h3 className="text-sm font-semibold text-slate-900">Data Coverage</h3>
            <ul className="mt-3 space-y-2 text-sm text-slate-500">
              <li>8 Malaysian Blue-Chip companies</li>
              <li>5-year historical financials</li>
              <li>Income statement data</li>
              <li>KPI summaries</li>
            </ul>
          </div>
        </div>

        <div className="mt-8 border-t border-slate-100 pt-6 text-center text-xs text-slate-400">
          © {new Date().getFullYear()} FinSight. Financial data is for informational purposes only.
        </div>
      </div>
    </footer>
  );
}
