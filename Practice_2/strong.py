def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res

def is_strong(n):
    if n < 0:
        return False
    s = str(n)
    sum_fact = 0
    for char in s:
        digit = int(char)
        sum_fact = sum_fact + factorial(digit)
    return sum_fact == n
