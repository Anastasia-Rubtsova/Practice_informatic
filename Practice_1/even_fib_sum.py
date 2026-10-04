def even_fib_sum(limit):
    a, b = 1, 2
    total_sum = 0

    while a <= limit:
        if a % 2 == 0:
            total_sum += a
        a, b = b, a + b

    return total_sum

try:
    limit = int(input("Введите максимальное значение числа (лимит): "))
    result = even_fib_sum(limit)
    print(f"Сумма чётных чисел равна: {result}")
except ValueError:
    print("Ошибка: введите целое число.")
