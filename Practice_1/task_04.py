# задача 4

def swap(a, b):
    return b, a

a = int(input("Введите число 1 для обмена с числом 2: "))
b = int(input("Введите число 2 для обмена с числом 1: "))
a, b = swap(a, b)
print(a, b)

