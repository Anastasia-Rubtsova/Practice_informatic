def square_digits(n):
    result = ''
    for char in str(n):
        digit = int(char)
        square = digit ** 2
        result += str(square)
    return result

try:
    n = input("Введите число для возведения цифр в квадрат: ")
    if not n.isdigit():
        print("Ошибка: введите только цифры.")
    else:
        result = square_digits(n)
        print("Результат:", result)
except Exception as e:
    print(f"Ошибка: {e}")
