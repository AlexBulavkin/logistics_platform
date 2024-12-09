from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    guid: str
    size: int


class DeliveryAddress(BaseModel):
    coordinates: List[float]
    products: List[dict]


class Warehouse(BaseModel):
    coordinates: List[float]
    products: List[str]


class LogisticsRequest(BaseModel):
    start_point: List[float]
    delivery_addresses: List[DeliveryAddress]
    warehouses: List[Warehouse]
    vehicle_capacity: int
