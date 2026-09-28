# задача 13

def multiplication_table(n):
    table = []
    for i in range(1, 11):
        result = n * i
        table.append(f"{n} x {i} = {result}")
    return table

user_number = int(input("Введите число для таблицы умножения: "))
my_table = multiplication_table(user_number)
for line in my_table:
    print(line)
