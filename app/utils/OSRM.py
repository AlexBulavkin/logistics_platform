import requests

point_a = [92.37641812698361, 55.96012740368077]
point_b = [92.37154582471588, 55.95859550543869]
response = requests.get(
    f"http://router.project-osrm.org/route/v1/car/{point_a[0]},{point_a[1]};{point_b[0]},{point_b[1]}"
).json()
print(response["routes"][0]["distance"])
# print(response)
# print(response['routes'])

# http://router.project-osrm.org/route/v1/car/92.37641812698361,55.96012740368077;92.37154582471588,55.95859550543869