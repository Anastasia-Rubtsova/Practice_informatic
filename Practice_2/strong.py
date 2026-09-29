number = int(input("Введите число, для проверки является ли оно сильным: "))

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_strong(number):
    digits = [int(d) for d in str(number)]
    result = sum(factorial(d) for d in digits)
    if result < number or result > number:
        print("False")
    else:
        print("True")

is_strong(number)
