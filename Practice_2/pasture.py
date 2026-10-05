def pasture_area(wire, w):
    l = (wire - 2 * w) / 3
    if l < 0:
        return 0.0
    return w * l


def best_pasture(wire):
    w_optimal = wire / 4
    l_optimal = (wire - 2 * w_optimal) / 3
    area_optimal = w_optimal * l_optimal
    return (w_optimal, l_optimal, area_optimal)


wire = float(input("Введите длину проволоки: "))
w = float(input("Введите ширину загона: "))

area = pasture_area(wire, w)
print(f"Площадь загона: {area}")

w_opt, l_opt, area_opt = best_pasture(wire)
print(f"Оптимальная ширина: {w_opt}")
print(f"Оптимальная длина: {l_opt}")
print(f"Максимальная площадь: {area_opt}")
