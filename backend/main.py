import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import companies, financials

app = FastAPI(
    title="FinSight API",
    description=(
        "Financial data API for Malaysian Blue-Chip companies. "
        "Provides company details, KPI summaries, and historical income statement data."
    ),
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# --- CORS ----------------------------------------------------------------
# Allow the Next.js frontend and any preview deployments.
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# --- Routers -------------------------------------------------------------
app.include_router(companies.router)
app.include_router(financials.router)


@app.get("/", tags=["health"])
def root():
    return {"status": "ok", "service": "FinSight API", "version": "0.1.0"}


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}
