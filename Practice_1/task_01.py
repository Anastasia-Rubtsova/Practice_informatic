# задача 1
def meters_to_centimeters(meters):
    centimeters = meters * 100
    return centimeters

meters = int(input("Введите метры, для перевода их в сантиметры: "))
result = meters_to_centimeters(meters)
print(f"Distance in centimeters: {result}")
