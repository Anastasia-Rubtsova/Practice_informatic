def knapsack_dp(items, capacity):
    dp = [0] * (capacity + 1)
    
    for weight, value in items:
        for c in range(capacity, weight - 1, -1):
            new_value = dp[c - weight] + value
            if new_value > dp[c]:
                dp[c] = new_value
    
    return dp[capacity]
