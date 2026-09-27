"""
FastAPI Application Entry Point.
"""

import os
from fastapi import FastAPI
from dotenv import load_dotenv

from api.middleware.cors import add_cors_middleware
from api.routes.arrange import router as arrange_router

load_dotenv()

app = FastAPI(
    title="AI Song Arrangement Assistant",
    description=(
        "Analyzes song lyrics using NLP to recommend instruments, genre, tempo, "
        "dynamics, and a complete band arrangement template."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS
allowed_origins = os.getenv(
    "ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:3000"
).split(",")
add_cors_middleware(app, allowed_origins)

# Routes
app.include_router(arrange_router, prefix="/api", tags=["Arrangement"])


@app.get("/api/health", tags=["Health"])
async def health():
    """Health check endpoint."""
    return {"status": "ok", "service": "AI Song Arrangement Assistant", "version": "1.0.0"}


@app.get("/", tags=["Root"])
async def root():
    return {"message": "AI Song Arrangement Assistant API. Visit /docs for documentation."}
