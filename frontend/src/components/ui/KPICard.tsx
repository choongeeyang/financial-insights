import { deltaColor, formatPct } from "@/lib/utils";

interface KPICardProps {
  label: string;
  value: string;
  delta?: number;
  subtitle?: string;
  highlight?: boolean;
}

export default function KPICard({
  label,
  value,
  delta,
  subtitle,
  highlight = false,
}: KPICardProps) {
  return (
    <div
      className={`rounded-xl border p-4 ${
        highlight
          ? "border-blue-200 bg-blue-50"
          : "border-slate-200 bg-white"
      }`}
    >
      <p className="text-xs font-medium uppercase tracking-wider text-slate-500">
        {label}
      </p>
      <p className="mt-1 text-2xl font-bold text-slate-900">{value}</p>
      {delta !== undefined && (
        <p className={`mt-1 text-sm font-medium ${deltaColor(delta)}`}>
          {delta >= 0 ? "▲" : "▼"} {formatPct(Math.abs(delta))} YoY
        </p>
      )}
      {subtitle && (
        <p className="mt-1 text-xs text-slate-400">{subtitle}</p>
      )}
    </div>
  );
}
