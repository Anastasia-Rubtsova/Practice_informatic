# задача 14 

def circle_diameter(radius):
    return radius * 2

def sum_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

radius = int(input("Введите радиус окружности: "))
print("Диаметр окружности:", circle_diameter(radius))

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
print("Сумма чисел в диапазоне:", sum_range(start, end))