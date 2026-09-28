# задача 7

def compare(m, n):
    if m > n:
        return "Number m > n"
    elif m < n:
        return "Number m < n"
    else:
        return "The numbers are equal"

m = int(input("Введите число m для сравнения: "))
n = int(input("Введите число n для сравнения: "))
print(compare(m, n))
