from fastapi import APIRouter, HTTPException
from data.mock_data import INCOME_STATEMENTS, COMPANIES
from schemas import IncomeStatementResponse, IncomeStatementEntry

router = APIRouter(prefix="/financials", tags=["financials"])


@router.get("/{ticker}/income-statement", response_model=IncomeStatementResponse)
def get_income_statement(ticker: str):
    """Return 5-year annual income statement data for a company."""
    key = ticker.upper()
    if key not in INCOME_STATEMENTS:
        raise HTTPException(status_code=404, detail=f"Financials for '{ticker}' not found.")
    company = COMPANIES[key]
    return IncomeStatementResponse(
        ticker=key,
        name=company["name"],
        currency=company["currency"],
        data=[IncomeStatementEntry(**entry) for entry in INCOME_STATEMENTS[key]],
    )
