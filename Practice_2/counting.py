def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res

def arrangements(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return factorial(n) // factorial(n - k)

def combinations(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res = res * (n - i) // (i + 1)
    return res
