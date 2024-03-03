from fastapi import FastAPI
from app.config.configs import settings
from fastapi.middleware.cors import CORSMiddleware


import app.api.v1.healthz as health_router
import app.api.v1.embeds as embeds_router


app =FastAPI(
    title=settings.PROJECT_TITLE,
    description=settings.PROJECT_DESC,
    openapi_url = f"{settings.API_V1_PREFIX}/openapi.json",
    docs_url= f"{settings.API_V1_PREFIX}/docs",
    redoc_url=f"{settings.API_V1_PREFIX}/redoc",
    debug=True
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Type", "Content-Disposition"]
)

app.include_router(health_router.router)
app.include_router(embeds_router.router)
