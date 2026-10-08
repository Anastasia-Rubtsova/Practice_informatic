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
        
        line = " ".join(week_row).rstrip()
        if line:
            calendar.append(line)
            
        if current_day > days:
            break
            
    return "\n".join(calendar)
