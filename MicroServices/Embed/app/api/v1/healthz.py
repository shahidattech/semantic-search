from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.config.configs import settings

router = APIRouter(
    tags=["Health"],
    prefix=settings.API_V1_PREFIX
)


@router.get("/health")
def healthCheck():
    return JSONResponse(status_code=200, content="service is up & running...")