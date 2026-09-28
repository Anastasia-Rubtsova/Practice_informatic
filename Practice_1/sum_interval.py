a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

def sum_interval(a, b):
    start = min(a, b)
    end = max(a, b)
    total = (start + end) * (end - start + 1) // 2
    return total

print("Расчёты сложения чисел с диапазона:", sum_interval(a, b))
