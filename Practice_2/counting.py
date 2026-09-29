# задача 4
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def arrangements(n, k):
    if n < 0 or k < 0 or k > n:
        return None
    return factorial(n) // factorial(n - k) 
    
def combinations(n, k):
    if n < 0 or k < 0 or k > n:
        return None
    return factorial(n) // (factorial(k) * factorial(n - k))

try:
    n = int(input("Введите целое число n : "))
    k = int(input("Введите целое число k : "))

    if n < 0 or k < 0 or k > n:
        print("Проверьте значения: n и k должны быть >= 0, а k не больше n.")
    else:
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

except NameError as e:
    print(f"Ошибка обращения к переменной: {e}")

except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
