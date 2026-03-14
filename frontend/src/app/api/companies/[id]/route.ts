import { NextRequest, NextResponse } from "next/server";

const BACKEND =
  process.env.INTERNAL_API_URL ??
  process.env.NEXT_PUBLIC_API_URL ??
  "http://localhost:8000";

export const revalidate = 3600;

export async function GET(
  _req: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params;
  const ticker = id.toUpperCase();

  try {
    const [companyRes, summaryRes] = await Promise.all([
      fetch(`${BACKEND}/companies/${ticker}`, { next: { revalidate: 3600 } }),
      fetch(`${BACKEND}/companies/${ticker}/summary`, { next: { revalidate: 3600 } }),
    ]);

    if (!companyRes.ok) {
      return NextResponse.json({ error: `Company '${ticker}' not found` }, { status: 404 });
    }

    const company = await companyRes.json();
    const summary = summaryRes.ok ? await summaryRes.json() : null;

    return NextResponse.json({ company, summary });
  } catch {
    return NextResponse.json({ error: "Backend unavailable" }, { status: 503 });
  }
}
