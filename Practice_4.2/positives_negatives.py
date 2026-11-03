def count_positives_sum_negatives(numbers):
    if not numbers:
        return []
    
    pos_count = 0
    neg_sum = 0
    for num in numbers:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_sum += num
    return [pos_count, neg_sum]
