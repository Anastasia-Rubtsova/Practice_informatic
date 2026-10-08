# задача 8

def century_message(name, age, current_year):
    year_100 = current_year + (100 - age)
    if age >= 100:
        return f"{name}, тебе уже 100 лет или даже больше (в {year_100} году)"
    return f"{name}, тебе исполнится 100 лет в {year_100} году"
