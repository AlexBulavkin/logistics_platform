from fastapi import APIRouter, Request
from app.schemas.misc_schemas import HealthcheckSchema
from config import settings

router = APIRouter()


@router.get("/healthcheck", response_model=HealthcheckSchema)
def healthcheck(request: Request):
    return HealthcheckSchema(status="OK", version=settings.app.app_version)
