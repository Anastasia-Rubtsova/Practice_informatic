# задача 3

def is_divisor(a, b):
    if a == 0:
        return False
    return b % a == 0

a = int(input("Введите число делитель: "))
b = int(input("Введите число делимое: "))
print(is_divisor(a, b))
