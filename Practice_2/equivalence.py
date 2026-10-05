def truth_table(n):
    if n == 0:
        return [()]
    result = []
    for i in range(2 ** n):
        binary = format(i, f'0{n}b')
        row = tuple(int(bit) for bit in binary)
        result.append(row)
    return result


def are_equivalent(f, g, n):
    table = truth_table(n)
    for row in table:
        if f(*row) != g(*row):
            return False
    return True

print("Выберите проверку:")
print("1 — Закон де Моргана")
print("2 — Закон де Моргана 2")
print("3 — Импликация")
print("4 — Контрапозиция")
choice = input("Введите номер (1–4): ")

if choice == "1":
    def f(a, b): return not (a and b)
    def g(a, b): return (not a) or (not b)
    n = 2
elif choice == "2":
    def f(a, b): return not (a or b)
    def g(a, b): return (not a) and (not b)
    n = 2
elif choice == "3":
    def implies(a, b): return (not a) or b
    def f(a, b): return implies(a, b)
    def g(a, b): return implies(a, b)  
    n = 2
elif choice == "4":
    def implies(a, b): return (not a) or b
    def contraposition(a, b): return implies(not b, not a)
    def f(a, b): return implies(a, b)
    def g(a, b): return contraposition(a, b)
    n = 2
else:
    raise ValueError("Неверный выбор")

if are_equivalent(f, g, n):
    print("Функции эквивалентны")
else:
    print("Функции НЕ эквивалентны")
