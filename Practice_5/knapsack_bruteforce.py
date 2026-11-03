def knapsack_bruteforce(items, capacity):
    def solve(index, current_weight, current_value):
        if index == len(items):
            return current_value        
        weight, value = items[index]
        best = solve(index + 1, current_weight, current_value)

        if current_weight + weight <= capacity:
            take = solve(index + 1, current_weight + weight, current_value + value)
            if take > best:
                best = take
        
        return best    
    return solve(0, 0, 0)
