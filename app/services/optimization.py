from typing import List, Tuple
from app.schemas.request import LogisticsRequest
from app.services.map_api import get_route_distance, generate_map_link


def calculate_optimal_route(request: LogisticsRequest) -> Tuple[List[List[float]], str]:
    # 1. Анализ данных (группировка товаров, проверка вместимости)
    deliveries = request.delivery_addresses
    warehouses = request.warehouses
    vehicle_capacity = request.vehicle_capacity

    # 2. Оптимизация маршрута
    # Заглушка - маршрут в порядке поступления и проверка работы get_route_distance

    route = [request.start_point]
    for warehouse in warehouses:
        route.append(warehouse.coordinates)
        warehouse_coordinates_last = warehouse.coordinates
    for delivery in deliveries:
        route.append(delivery.coordinates)
    route.append(request.start_point)  # Возврат в начальную точку

    # Проверка работы get_route_distance
    distance = [
        get_route_distance(request.start_point, warehouse_coordinates_last),
        get_route_distance(request.start_point, warehouse_coordinates_last),
    ]
    route.append(distance)

    # 3. Генерация ссылки на карту
    map_link = generate_map_link(route)

    return route, map_link
