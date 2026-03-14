from pydantic import BaseModel
from typing import Optional


class CompanySummary(BaseModel):
    ticker: str
    name: str
    sector: str
    market_cap_bln: float
    currency: str = "MYR"


class CompanyDetail(BaseModel):
    ticker: str
    name: str
    sector: str
    industry: str
    description: str
    market_cap_bln: float
    employees: int
    founded: int
    headquarters: str
    website: str
    currency: str = "MYR"
    exchange: str = "KLSE"


class KPISummary(BaseModel):
    ticker: str
    revenue_bln: float
    net_income_bln: float
    eps: float
    pe_ratio: Optional[float]
    roe_pct: float
    debt_to_equity: float
    dividend_yield_pct: Optional[float]
    fiscal_year: int


class IncomeStatementEntry(BaseModel):
    fiscal_year: int
    revenue_bln: float
    gross_profit_bln: float
    operating_income_bln: float
    net_income_bln: float
    eps: float
    gross_margin_pct: float
    operating_margin_pct: float
    net_margin_pct: float


class IncomeStatementResponse(BaseModel):
    ticker: str
    name: str
    currency: str
    data: list[IncomeStatementEntry]
