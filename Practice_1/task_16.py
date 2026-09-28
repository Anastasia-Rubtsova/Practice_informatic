# задача 16

def month_calendar(start_weekday, days):
    calendar = []
    current_day = 1

    for week in range(6):
        week_row = []
        for day_of_week in range(7):
            if week == 0 and day_of_week < start_weekday:
                week_row.append("  ")
            elif current_day <= days:
                week_row.append(f"{current_day:2}")
                current_day += 1
            else:
                week_row.append("  ")

        # Проверяем, есть ли в неделе реальные дни
        if any(day != "  " for day in week_row):
            calendar.append(" ".join(week_row))

    return "\n".join(calendar)

start_weekday = int(input("Введите день недели для 1-го числа (0 — понедельник, 6 — воскресенье): "))
days = int(input("Введите количество дней в месяце: "))
print(month_calendar(start_weekday, days))

