# задача 15

def days_in_month(month, year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
    return days[month - 1]

user_month = int(input("Введите номер месяца (1-12): "))
user_year = int(input("Введите четырехзначный год: "))
result = days_in_month(user_month, user_year)
print(f"Количество дней в этом месяце: {result}")
