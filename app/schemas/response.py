from pydantic import BaseModel
from typing import List


class LogisticsResponse(BaseModel):
    route: List[List[float]]
    map_link: str
