def min_pair_sum(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    total = 0
    for i in range(n // 2):
        total += sorted_nums[i] * sorted_nums[n - 1 - i]
        
    return total
