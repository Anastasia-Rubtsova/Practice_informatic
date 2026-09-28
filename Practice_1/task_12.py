# задача 12

def shortest_distance(kilometers, meters):
    km_in_meters = kilometers * 1000
    return min(km_in_meters, meters)

user_km = int(input("Введите расстояние в километрах: "))
user_m = int(input("Введите расстояние в метрах: "))
result = shortest_distance(user_km, user_m)
print(f"Наименьшее расстояние в метрах: {result}")
