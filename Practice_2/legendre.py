def max_power(n, k):
    deliteli = {}
    temp = k
    d = 2
    
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count = count + 1
                temp = temp // d
            deliteli[d] = count
        d = d + 1
    
    if temp > 1:
        deliteli[temp] = 1
    
    min_step = -1
    
    for p in deliteli:
        step_v_k = deliteli[p]
        count_in_fact = 0
        current_power = p
        
        while current_power <= n:
            count_in_fact = count_in_fact + (n // current_power)
            current_power = current_power * p
        
        groups = count_in_fact // step_v_k
        
        if min_step == -1 or groups < min_step:
            min_step = groups
    
    return min_step
