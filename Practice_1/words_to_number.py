from enum import IntEnum

class NumberWord(IntEnum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven = 11
    twelve = 12
    thirteen = 13
    fourteen = 14
    fifteen = 15
    sixteen = 16
    seventeen = 17
    eighteen = 18
    nineteen = 19
    twenty = 20
    thirty = 30
    forty = 40
    fifty = 50
    sixty = 60
    seventy = 70
    eighty = 80
    ninety = 90

def words_to_number(text):
    text = text.replace("-", " ").replace("and", "").lower()
    words = text.split()
    total = 0
    current = 0
    for word in words:
        word = word.strip()
        if word == "hundred":
            current *= 100
        elif word == "thousand":
            total += current * 1000
            current = 0
        elif word == "million":
            total = current * 1_000_000
            current = 0
        elif word in NumberWord.__members__:
            current += NumberWord[word].value
    return total + current

text = input("Введите число словами: ")
try:
    print(f"Результат: {words_to_number(text)}")
except Exception as e:
    print(f"Ошибка: {e}")
