/** Format a number in billions to a readable string. e.g. 12.3 → "MYR 12.3B" */
export function formatBillions(value: number, currency = "MYR"): string {
  return `${currency} ${value.toFixed(1)}B`;
}

/** Format a percentage. e.g. 28.4 → "28.4%" */
export function formatPct(value: number): string {
  return `${value.toFixed(1)}%`;
}

/** Format large numbers with locale separators */
export function formatNumber(value: number): string {
  return value.toLocaleString("en-MY");
}

/** Return a Tailwind color class based on numeric delta sign */
export function deltaColor(delta: number): string {
  if (delta > 0) return "text-emerald-600";
  if (delta < 0) return "text-red-500";
  return "text-slate-500";
}

/** Compute year-over-year % change */
export function yoyChange(current: number, previous: number): number {
  if (previous === 0) return 0;
  return ((current - previous) / Math.abs(previous)) * 100;
}

/** Sector color mapping */
const SECTOR_COLORS: Record<string, string> = {
  Financials: "bg-blue-100 text-blue-700",
  Utilities: "bg-yellow-100 text-yellow-700",
  Energy: "bg-orange-100 text-orange-700",
  "Communication Services": "bg-purple-100 text-purple-700",
  "Consumer Discretionary": "bg-pink-100 text-pink-700",
  "Real Estate": "bg-teal-100 text-teal-700",
};

export function sectorBadgeClass(sector: string): string {
  return SECTOR_COLORS[sector] ?? "bg-slate-100 text-slate-700";
}
