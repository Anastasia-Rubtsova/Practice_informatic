n = input("Введите в строку числа для возведения в квадрат и дальнейшей склейки: ")

def square_digits(n):
    result = ''
    for char in n:
        digit = int(char)
        square = digit ** 2
        result += str(square)
    return result

print("Результат:", square_digits(n))
