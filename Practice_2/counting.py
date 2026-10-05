def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def arrangements(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return factorial(n) // factorial(n - k)

def combinations(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    # Оптимизированный расчёт сочетаний
    if k > n - k:
        k = n - k
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

try:
    n = int(input("Введите целое число n: "))
    k = int(input("Введите целое число k: "))

    res_fact_n = factorial(n)
    res_fact_k = factorial(k)
    res_arr = arrangements(n, k)
    res_comb = combinations(n, k)

    print(f"Факториал числа {n} равен: {res_fact_n}")
    print(f"Факториал числа {k} равен: {res_fact_k}")
    print(f"Размещения A({n}, {k}): {res_arr}")
    print(f"Сочетания C({n}, {k}): {res_comb}")

except ValueError:
    print("Ошибка: Вы ввели некорректные данные! Пожалуйста, вводите только целые числа.")
