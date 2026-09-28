# задача 9

def max_of_three(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num

a = int(input("Введите число a для сравнения: "))
b = int(input("Введите число b для сравнения: "))
c = int(input("Введите число c для сравнения: "))
print("Наибольшее число:", max_of_three(a, b, c))
