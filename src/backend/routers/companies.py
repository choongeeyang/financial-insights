from fastapi import APIRouter, HTTPException
from data.mock_data import COMPANIES, KPI_SUMMARIES
from schemas import CompanySummary, CompanyDetail, KPISummary

router = APIRouter(prefix="/companies", tags=["companies"])


@router.get("", response_model=list[CompanySummary])
def list_companies():
    """Return a summary list of all available companies."""
    return [
        CompanySummary(
            ticker=c["ticker"],
            name=c["name"],
            sector=c["sector"],
            market_cap_bln=c["market_cap_bln"],
            currency=c["currency"],
        )
        for c in COMPANIES.values()
    ]


@router.get("/{ticker}", response_model=CompanyDetail)
def get_company(ticker: str):
    """Return full detail for a single company by ticker symbol."""
    key = ticker.upper()
    if key not in COMPANIES:
        raise HTTPException(status_code=404, detail=f"Company '{ticker}' not found.")
    return CompanyDetail(**COMPANIES[key])


@router.get("/{ticker}/summary", response_model=KPISummary)
def get_company_summary(ticker: str):
    """Return KPI summary (revenue, net income, EPS, ROE, etc.) for a company."""
    key = ticker.upper()
    if key not in KPI_SUMMARIES:
        raise HTTPException(status_code=404, detail=f"Company '{ticker}' not found.")
    return KPISummary(**KPI_SUMMARIES[key])
