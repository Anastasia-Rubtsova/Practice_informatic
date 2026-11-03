def greedy_knapsack(items, capacity):
    def get_cost(item):
        return item[1]
    
    sorted_items = sorted(items, key=get_cost, reverse=True)
    
    total_weight = 0
    total_value = 0
    
    for weight, value in sorted_items:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
    
    return total_value
