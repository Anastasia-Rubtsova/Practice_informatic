def integer_square_root(n):
    low = 0
    high = n
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            ans = mid
            low = mid + 1  # Пробуем найти число побольше
        else:
            high = mid - 1
            
    return ans
