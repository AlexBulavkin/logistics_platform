from fastapi import APIRouter, HTTPException
from app.schemas.request import LogisticsRequest
from app.schemas.response import LogisticsResponse
from app.services.optimization import calculate_optimal_route

router = APIRouter(prefix="/logistics", tags=["Logistics"])


@router.post("/optimize", response_model=LogisticsResponse)
async def optimize_route(request: LogisticsRequest):
    try:
        route, map_link = calculate_optimal_route(request)
        return {"route": route, "map_link": map_link}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
