"""
Mock financial data for 8 Malaysian Blue-Chip companies (KLSE).
All monetary values in MYR billions unless noted otherwise.
Figures are illustrative and based on approximate public data.
"""

COMPANIES: dict = {
    "MAYBANK": {
        "ticker": "MAYBANK",
        "name": "Malayan Banking Berhad",
        "sector": "Financials",
        "industry": "Banking",
        "description": (
            "Maybank is Malaysia's largest bank and one of the leading financial services "
            "groups in ASEAN. It offers a comprehensive range of financial products and "
            "services including commercial banking, investment banking, insurance, and "
            "Islamic finance across 20 countries."
        ),
        "market_cap_bln": 102.4,
        "employees": 43000,
        "founded": 1960,
        "headquarters": "Kuala Lumpur, Malaysia",
        "website": "https://www.maybank.com",
        "currency": "MYR",
        "exchange": "KLSE",
    },
    "CIMB": {
        "ticker": "CIMB",
        "name": "CIMB Group Holdings Berhad",
        "sector": "Financials",
        "industry": "Banking",
        "description": (
            "CIMB Group is one of ASEAN's leading universal banking groups, offering "
            "consumer banking, commercial banking, investment banking, and asset management "
            "services across 18 countries with over 34,000 employees."
        ),
        "market_cap_bln": 62.1,
        "employees": 34000,
        "founded": 1924,
        "headquarters": "Kuala Lumpur, Malaysia",
        "website": "https://www.cimb.com",
        "currency": "MYR",
        "exchange": "KLSE",
    },
    "TNB": {
        "ticker": "TNB",
        "name": "Tenaga Nasional Berhad",
        "sector": "Utilities",
        "industry": "Electric Utilities",
        "description": (
            "Tenaga Nasional Berhad is Malaysia's largest electricity utility company and "
            "one of the largest in Southeast Asia. TNB is involved in the generation, "
            "transmission, and distribution of electricity throughout Peninsular Malaysia."
        ),
        "market_cap_bln": 78.3,
        "employees": 35000,
        "founded": 1990,
        "headquarters": "Kuala Lumpur, Malaysia",
        "website": "https://www.tnb.com.my",
        "currency": "MYR",
        "exchange": "KLSE",
    },
    "PETRONAS": {
        "ticker": "PETRONAS",
        "name": "Petroliam Nasional Berhad",
        "sector": "Energy",
        "industry": "Integrated Oil & Gas",
        "description": (
            "PETRONAS is Malaysia's national oil company, wholly owned by the Malaysian "
            "government. It is engaged in the exploration, development, and production of "
            "oil and natural gas resources globally, as well as downstream chemicals and "
            "retail fuel operations."
        ),
        "market_cap_bln": 320.0,
        "employees": 51000,
        "founded": 1974,
        "headquarters": "Kuala Lumpur, Malaysia",
        "website": "https://www.petronas.com",
        "currency": "MYR",
        "exchange": "Private",
    },
    "MAXIS": {
        "ticker": "MAXIS",
        "name": "Maxis Berhad",
        "sector": "Communication Services",
        "industry": "Telecommunications",
        "description": (
            "Maxis is Malaysia's leading telecommunications company, providing mobile, "
            "fixed-line, broadband, and enterprise solutions. It serves millions of "
            "individual and business customers across Malaysia with a focus on 5G and "
            "digital services."
        ),
        "market_cap_bln": 36.2,
        "employees": 5000,
        "founded": 1993,
        "headquarters": "Kuala Lumpur, Malaysia",
        "website": "https://www.maxis.com.my",
        "currency": "MYR",
        "exchange": "KLSE",
    },
    "TM": {
        "ticker": "TM",
        "name": "Telekom Malaysia Berhad",
        "sector": "Communication Services",
        "industry": "Integrated Telecommunications",
        "description": (
            "Telekom Malaysia is Malaysia's incumbent telecommunications company and the "
            "country's largest fixed-line operator. TM provides broadband, voice, data, "
            "and managed services to consumers and enterprises, operating the national "
            "fibre broadband infrastructure."
        ),
        "market_cap_bln": 24.8,
        "employees": 21000,
        "founded": 1984,
        "headquarters": "Kuala Lumpur, Malaysia",
        "website": "https://www.tm.com.my",
        "currency": "MYR",
        "exchange": "KLSE",
    },
    "GENTING": {
        "ticker": "GENTING",
        "name": "Genting Berhad",
        "sector": "Consumer Discretionary",
        "industry": "Casinos & Gaming",
        "description": (
            "Genting Berhad is a global leisure and hospitality corporation with businesses "
            "in leisure and hospitality, power generation, oil and gas, and plantations. "
            "It operates resorts and casinos across Malaysia, Singapore, the US, and UK "
            "through its listed subsidiaries."
        ),
        "market_cap_bln": 22.6,
        "employees": 60000,
        "founded": 1965,
        "headquarters": "Kuala Lumpur, Malaysia",
        "website": "https://www.genting.com",
        "currency": "MYR",
        "exchange": "KLSE",
    },
    "SUNWAY": {
        "ticker": "SUNWAY",
        "name": "Sunway Berhad",
        "sector": "Real Estate",
        "industry": "Diversified Real Estate",
        "description": (
            "Sunway Berhad is one of Malaysia's largest conglomerates with diversified "
            "businesses in property development, construction, hospitality, retail, "
            "education, and healthcare. It is known for developing integrated townships "
            "including the Sunway City township in Selangor."
        ),
        "market_cap_bln": 18.4,
        "employees": 16000,
        "founded": 1974,
        "headquarters": "Petaling Jaya, Malaysia",
        "website": "https://www.sunway.com.my",
        "currency": "MYR",
        "exchange": "KLSE",
    },
}

KPI_SUMMARIES: dict = {
    "MAYBANK": {
        "ticker": "MAYBANK",
        "revenue_bln": 30.2,
        "net_income_bln": 9.1,
        "eps": 0.86,
        "pe_ratio": 12.4,
        "roe_pct": 10.8,
        "debt_to_equity": 0.92,
        "dividend_yield_pct": 5.8,
        "fiscal_year": 2024,
    },
    "CIMB": {
        "ticker": "CIMB",
        "revenue_bln": 22.4,
        "net_income_bln": 6.3,
        "eps": 0.62,
        "pe_ratio": 10.2,
        "roe_pct": 11.2,
        "debt_to_equity": 1.05,
        "dividend_yield_pct": 5.1,
        "fiscal_year": 2024,
    },
    "TNB": {
        "ticker": "TNB",
        "revenue_bln": 58.7,
        "net_income_bln": 3.8,
        "eps": 0.67,
        "pe_ratio": 18.6,
        "roe_pct": 6.4,
        "debt_to_equity": 1.42,
        "dividend_yield_pct": 3.2,
        "fiscal_year": 2024,
    },
    "PETRONAS": {
        "ticker": "PETRONAS",
        "revenue_bln": 320.0,
        "net_income_bln": 55.0,
        "eps": 6.22,
        "pe_ratio": None,
        "roe_pct": 14.5,
        "debt_to_equity": 0.28,
        "dividend_yield_pct": None,
        "fiscal_year": 2024,
    },
    "MAXIS": {
        "ticker": "MAXIS",
        "revenue_bln": 9.8,
        "net_income_bln": 1.6,
        "eps": 0.20,
        "pe_ratio": 22.1,
        "roe_pct": 31.4,
        "debt_to_equity": 2.18,
        "dividend_yield_pct": 3.7,
        "fiscal_year": 2024,
    },
    "TM": {
        "ticker": "TM",
        "revenue_bln": 12.3,
        "net_income_bln": 1.1,
        "eps": 0.29,
        "pe_ratio": 14.8,
        "roe_pct": 8.9,
        "debt_to_equity": 1.12,
        "dividend_yield_pct": 4.2,
        "fiscal_year": 2024,
    },
    "GENTING": {
        "ticker": "GENTING",
        "revenue_bln": 21.4,
        "net_income_bln": 1.9,
        "eps": 0.52,
        "pe_ratio": 11.6,
        "roe_pct": 5.8,
        "debt_to_equity": 0.76,
        "dividend_yield_pct": 2.1,
        "fiscal_year": 2024,
    },
    "SUNWAY": {
        "ticker": "SUNWAY",
        "revenue_bln": 8.6,
        "net_income_bln": 1.0,
        "eps": 0.47,
        "pe_ratio": 13.4,
        "roe_pct": 9.3,
        "debt_to_equity": 0.58,
        "dividend_yield_pct": 3.6,
        "fiscal_year": 2024,
    },
}

INCOME_STATEMENTS: dict = {
    "MAYBANK": [
        {"fiscal_year": 2020, "revenue_bln": 24.8, "gross_profit_bln": 16.2, "operating_income_bln": 10.1, "net_income_bln": 6.5, "eps": 0.62, "gross_margin_pct": 65.3, "operating_margin_pct": 40.7, "net_margin_pct": 26.2},
        {"fiscal_year": 2021, "revenue_bln": 25.6, "gross_profit_bln": 17.0, "operating_income_bln": 10.8, "net_income_bln": 7.2, "eps": 0.68, "gross_margin_pct": 66.4, "operating_margin_pct": 42.2, "net_margin_pct": 28.1},
        {"fiscal_year": 2022, "revenue_bln": 27.4, "gross_profit_bln": 18.3, "operating_income_bln": 11.6, "net_income_bln": 7.9, "eps": 0.75, "gross_margin_pct": 66.8, "operating_margin_pct": 42.3, "net_margin_pct": 28.8},
        {"fiscal_year": 2023, "revenue_bln": 29.1, "gross_profit_bln": 19.8, "operating_income_bln": 12.4, "net_income_bln": 8.6, "eps": 0.81, "gross_margin_pct": 68.0, "operating_margin_pct": 42.6, "net_margin_pct": 29.6},
        {"fiscal_year": 2024, "revenue_bln": 30.2, "gross_profit_bln": 20.6, "operating_income_bln": 13.1, "net_income_bln": 9.1, "eps": 0.86, "gross_margin_pct": 68.2, "operating_margin_pct": 43.4, "net_margin_pct": 30.1},
    ],
    "CIMB": [
        {"fiscal_year": 2020, "revenue_bln": 17.2, "gross_profit_bln": 10.8, "operating_income_bln": 5.8, "net_income_bln": 3.1, "eps": 0.31, "gross_margin_pct": 62.8, "operating_margin_pct": 33.7, "net_margin_pct": 18.0},
        {"fiscal_year": 2021, "revenue_bln": 18.6, "gross_profit_bln": 11.9, "operating_income_bln": 6.6, "net_income_bln": 4.3, "eps": 0.43, "gross_margin_pct": 64.0, "operating_margin_pct": 35.5, "net_margin_pct": 23.1},
        {"fiscal_year": 2022, "revenue_bln": 20.1, "gross_profit_bln": 13.0, "operating_income_bln": 7.4, "net_income_bln": 5.2, "eps": 0.51, "gross_margin_pct": 64.7, "operating_margin_pct": 36.8, "net_margin_pct": 25.9},
        {"fiscal_year": 2023, "revenue_bln": 21.5, "gross_profit_bln": 13.9, "operating_income_bln": 8.1, "net_income_bln": 5.9, "eps": 0.58, "gross_margin_pct": 64.7, "operating_margin_pct": 37.7, "net_margin_pct": 27.4},
        {"fiscal_year": 2024, "revenue_bln": 22.4, "gross_profit_bln": 14.6, "operating_income_bln": 8.8, "net_income_bln": 6.3, "eps": 0.62, "gross_margin_pct": 65.2, "operating_margin_pct": 39.3, "net_margin_pct": 28.1},
    ],
    "TNB": [
        {"fiscal_year": 2020, "revenue_bln": 46.3, "gross_profit_bln": 14.2, "operating_income_bln": 7.1, "net_income_bln": 2.8, "eps": 0.49, "gross_margin_pct": 30.7, "operating_margin_pct": 15.3, "net_margin_pct": 6.0},
        {"fiscal_year": 2021, "revenue_bln": 50.1, "gross_profit_bln": 15.4, "operating_income_bln": 7.8, "net_income_bln": 3.1, "eps": 0.55, "gross_margin_pct": 30.7, "operating_margin_pct": 15.6, "net_margin_pct": 6.2},
        {"fiscal_year": 2022, "revenue_bln": 54.2, "gross_profit_bln": 16.1, "operating_income_bln": 8.2, "net_income_bln": 3.4, "eps": 0.60, "gross_margin_pct": 29.7, "operating_margin_pct": 15.1, "net_margin_pct": 6.3},
        {"fiscal_year": 2023, "revenue_bln": 56.8, "gross_profit_bln": 16.9, "operating_income_bln": 8.6, "net_income_bln": 3.6, "eps": 0.64, "gross_margin_pct": 29.8, "operating_margin_pct": 15.1, "net_margin_pct": 6.3},
        {"fiscal_year": 2024, "revenue_bln": 58.7, "gross_profit_bln": 17.8, "operating_income_bln": 9.1, "net_income_bln": 3.8, "eps": 0.67, "gross_margin_pct": 30.3, "operating_margin_pct": 15.5, "net_margin_pct": 6.5},
    ],
    "PETRONAS": [
        {"fiscal_year": 2020, "revenue_bln": 198.0, "gross_profit_bln": 62.4, "operating_income_bln": 28.1, "net_income_bln": 15.2, "eps": 1.72, "gross_margin_pct": 31.5, "operating_margin_pct": 14.2, "net_margin_pct": 7.7},
        {"fiscal_year": 2021, "revenue_bln": 245.0, "gross_profit_bln": 82.0, "operating_income_bln": 42.0, "net_income_bln": 30.0, "eps": 3.39, "gross_margin_pct": 33.5, "operating_margin_pct": 17.1, "net_margin_pct": 12.2},
        {"fiscal_year": 2022, "revenue_bln": 332.0, "gross_profit_bln": 124.0, "operating_income_bln": 78.0, "net_income_bln": 60.0, "eps": 6.78, "gross_margin_pct": 37.3, "operating_margin_pct": 23.5, "net_margin_pct": 18.1},
        {"fiscal_year": 2023, "revenue_bln": 296.0, "gross_profit_bln": 104.0, "operating_income_bln": 63.0, "net_income_bln": 49.0, "eps": 5.54, "gross_margin_pct": 35.1, "operating_margin_pct": 21.3, "net_margin_pct": 16.6},
        {"fiscal_year": 2024, "revenue_bln": 320.0, "gross_profit_bln": 112.0, "operating_income_bln": 70.0, "net_income_bln": 55.0, "eps": 6.22, "gross_margin_pct": 35.0, "operating_margin_pct": 21.9, "net_margin_pct": 17.2},
    ],
    "MAXIS": [
        {"fiscal_year": 2020, "revenue_bln": 8.4, "gross_profit_bln": 4.8, "operating_income_bln": 2.1, "net_income_bln": 1.2, "eps": 0.15, "gross_margin_pct": 57.1, "operating_margin_pct": 25.0, "net_margin_pct": 14.3},
        {"fiscal_year": 2021, "revenue_bln": 8.7, "gross_profit_bln": 5.0, "operating_income_bln": 2.2, "net_income_bln": 1.3, "eps": 0.16, "gross_margin_pct": 57.5, "operating_margin_pct": 25.3, "net_margin_pct": 14.9},
        {"fiscal_year": 2022, "revenue_bln": 9.1, "gross_profit_bln": 5.3, "operating_income_bln": 2.4, "net_income_bln": 1.4, "eps": 0.18, "gross_margin_pct": 58.2, "operating_margin_pct": 26.4, "net_margin_pct": 15.4},
        {"fiscal_year": 2023, "revenue_bln": 9.5, "gross_profit_bln": 5.6, "operating_income_bln": 2.6, "net_income_bln": 1.5, "eps": 0.19, "gross_margin_pct": 58.9, "operating_margin_pct": 27.4, "net_margin_pct": 15.8},
        {"fiscal_year": 2024, "revenue_bln": 9.8, "gross_profit_bln": 5.9, "operating_income_bln": 2.8, "net_income_bln": 1.6, "eps": 0.20, "gross_margin_pct": 60.2, "operating_margin_pct": 28.6, "net_margin_pct": 16.3},
    ],
    "TM": [
        {"fiscal_year": 2020, "revenue_bln": 10.8, "gross_profit_bln": 4.3, "operating_income_bln": 1.6, "net_income_bln": 0.7, "eps": 0.19, "gross_margin_pct": 39.8, "operating_margin_pct": 14.8, "net_margin_pct": 6.5},
        {"fiscal_year": 2021, "revenue_bln": 11.2, "gross_profit_bln": 4.6, "operating_income_bln": 1.8, "net_income_bln": 0.8, "eps": 0.21, "gross_margin_pct": 41.1, "operating_margin_pct": 16.1, "net_margin_pct": 7.1},
        {"fiscal_year": 2022, "revenue_bln": 11.7, "gross_profit_bln": 5.0, "operating_income_bln": 2.0, "net_income_bln": 0.9, "eps": 0.24, "gross_margin_pct": 42.7, "operating_margin_pct": 17.1, "net_margin_pct": 7.7},
        {"fiscal_year": 2023, "revenue_bln": 12.0, "gross_profit_bln": 5.2, "operating_income_bln": 2.1, "net_income_bln": 1.0, "eps": 0.26, "gross_margin_pct": 43.3, "operating_margin_pct": 17.5, "net_margin_pct": 8.3},
        {"fiscal_year": 2024, "revenue_bln": 12.3, "gross_profit_bln": 5.5, "operating_income_bln": 2.3, "net_income_bln": 1.1, "eps": 0.29, "gross_margin_pct": 44.7, "operating_margin_pct": 18.7, "net_margin_pct": 8.9},
    ],
    "GENTING": [
        {"fiscal_year": 2020, "revenue_bln": 10.1, "gross_profit_bln": 2.4, "operating_income_bln": 0.4, "net_income_bln": -1.2, "eps": -0.33, "gross_margin_pct": 23.8, "operating_margin_pct": 4.0, "net_margin_pct": -11.9},
        {"fiscal_year": 2021, "revenue_bln": 12.6, "gross_profit_bln": 3.8, "operating_income_bln": 1.2, "net_income_bln": 0.2, "eps": 0.05, "gross_margin_pct": 30.2, "operating_margin_pct": 9.5, "net_margin_pct": 1.6},
        {"fiscal_year": 2022, "revenue_bln": 17.8, "gross_profit_bln": 6.2, "operating_income_bln": 2.6, "net_income_bln": 1.2, "eps": 0.33, "gross_margin_pct": 34.8, "operating_margin_pct": 14.6, "net_margin_pct": 6.7},
        {"fiscal_year": 2023, "revenue_bln": 20.1, "gross_profit_bln": 7.4, "operating_income_bln": 3.1, "net_income_bln": 1.6, "eps": 0.44, "gross_margin_pct": 36.8, "operating_margin_pct": 15.4, "net_margin_pct": 8.0},
        {"fiscal_year": 2024, "revenue_bln": 21.4, "gross_profit_bln": 8.0, "operating_income_bln": 3.5, "net_income_bln": 1.9, "eps": 0.52, "gross_margin_pct": 37.4, "operating_margin_pct": 16.4, "net_margin_pct": 8.9},
    ],
    "SUNWAY": [
        {"fiscal_year": 2020, "revenue_bln": 5.8, "gross_profit_bln": 1.4, "operating_income_bln": 0.5, "net_income_bln": 0.3, "eps": 0.14, "gross_margin_pct": 24.1, "operating_margin_pct": 8.6, "net_margin_pct": 5.2},
        {"fiscal_year": 2021, "revenue_bln": 6.4, "gross_profit_bln": 1.7, "operating_income_bln": 0.7, "net_income_bln": 0.5, "eps": 0.23, "gross_margin_pct": 26.6, "operating_margin_pct": 10.9, "net_margin_pct": 7.8},
        {"fiscal_year": 2022, "revenue_bln": 7.3, "gross_profit_bln": 2.1, "operating_income_bln": 0.9, "net_income_bln": 0.7, "eps": 0.33, "gross_margin_pct": 28.8, "operating_margin_pct": 12.3, "net_margin_pct": 9.6},
        {"fiscal_year": 2023, "revenue_bln": 8.0, "gross_profit_bln": 2.4, "operating_income_bln": 1.1, "net_income_bln": 0.9, "eps": 0.42, "gross_margin_pct": 30.0, "operating_margin_pct": 13.8, "net_margin_pct": 11.3},
        {"fiscal_year": 2024, "revenue_bln": 8.6, "gross_profit_bln": 2.7, "operating_income_bln": 1.2, "net_income_bln": 1.0, "eps": 0.47, "gross_margin_pct": 31.4, "operating_margin_pct": 14.0, "net_margin_pct": 11.6},
    ],
}
