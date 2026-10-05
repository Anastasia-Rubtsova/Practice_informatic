def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_strong(number):
    if number < 0:
        return False
    digits = [int(d) for d in str(number)]
    result = sum(factorial(d) for d in digits)
    return result == number

try:
    number = int(input("Введите число, для проверки является ли оно сильным: "))
    if is_strong(number):
        print("True")
    else:
        print("False")
except ValueError:
    print("Ошибка: Введите корректное целое число.")
