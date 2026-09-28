# задача 11

import random

def guests_by_seat(seats):
    n = len(seats)
    result = [0] * n
    for k in range(n):
        result[seats[k] - 1] = k + 1
    return result

N = int(input("Введите количество мест, которые будут занимать гости: "))
if 0 < N <= 20000:
    random_seats = random.sample(range(1, N + 1), N)
    guests_order = guests_by_seat(random_seats)
    print("Рандомные места (вход):", random_seats)
    print("Кто где сидит (ответ):", guests_order)
else:
    print("Неверное количество мест (должно быть от 1 до 20 000)")
