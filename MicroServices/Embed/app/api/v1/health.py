from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    tags=["Health"],
    prefix="/skills/api/v1"
)


@router.get("/health")
def healthCheck():
    return JSONResponse(status_code=200, content="service is up & running...")