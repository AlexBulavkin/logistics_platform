from typing import List
import requests


def get_route_distance(point_a: List, point_b: List) -> float:
    response = requests.get(
        f"http://router.project-osrm.org/route/v1/car/{point_a[0]},{point_a[1]};{point_b[0]},{point_b[1]}"
    ).json()
    distance = response["routes"][0]["distance"]
    return distance


def generate_map_link(route: List[List[float]]) -> str:
    # Генерация ссылки для отображения маршрута на карте
    # Необходимо реализовать
    # для яндекса
    coordinates_str = "~".join([f"{coord[0]},{coord[1]}" for coord in route]) 
    return f"https://yandex.ru/maps/?rtext={coordinates_str}&rtt=auto"
    # для OSM
    # coordinates_str = ";".join([f"{coord[0]},{coord[1]}" for coord in route])
    # return f"https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&route={coordinates_str}#map=13/{route[0][0]}/{route[0][1]}"


