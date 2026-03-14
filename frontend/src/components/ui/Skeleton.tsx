interface SkeletonProps {
  className?: string;
}

export function Skeleton({ className = "" }: SkeletonProps) {
  return (
    <div
      className={`animate-pulse rounded-md bg-slate-200 ${className}`}
    />
  );
}

export function KPICardSkeleton() {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-4">
      <Skeleton className="h-3 w-20" />
      <Skeleton className="mt-2 h-8 w-28" />
      <Skeleton className="mt-2 h-3 w-16" />
    </div>
  );
}

export function CompanyCardSkeleton() {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5">
      <Skeleton className="h-5 w-20" />
      <Skeleton className="mt-2 h-4 w-36" />
      <div className="mt-3 flex justify-between">
        <Skeleton className="h-5 w-24" />
        <Skeleton className="h-5 w-20" />
      </div>
    </div>
  );
}

export function ChartSkeleton() {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-4">
      <Skeleton className="h-5 w-32 mb-4" />
      <Skeleton className="h-56 w-full" />
    </div>
  );
}

export function TableSkeleton() {
  return (
    <div className="rounded-xl border border-slate-200 bg-white overflow-hidden">
      <div className="p-4 border-b border-slate-100">
        <Skeleton className="h-5 w-40" />
      </div>
      <div className="p-4 space-y-3">
        {Array.from({ length: 5 }).map((_, i) => (
          <Skeleton key={i} className="h-8 w-full" />
        ))}
      </div>
    </div>
  );
}
