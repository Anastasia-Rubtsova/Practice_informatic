# задача 8

from datetime import date

def century_message(name, age, current_year):
    if age >= 100:
        print(f"Тебе {name}, уже 100 лет или даже больше")
    else:
        year_100 = current_year + (100 - age)
        print(f"Тебе {name}, исполнится 100 лет в {year_100}")

name = input("Введите свое имя: ")
age = int(input("Введите свой возраст: "))
current_year = date.today().year
century_message(name, age, current_year)
